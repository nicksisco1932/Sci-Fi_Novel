"""Generate "Stack Field: Rainline", a seamless slow ambient music loop.

The arrangement is music-first: sustained synth harmony, warm bass, sparse
electric-key tones, and distant melodic swells. It contains no broadband noise,
rain recording, drum pattern, or arpeggiator.
"""

from __future__ import annotations

import argparse
import subprocess
import wave
from pathlib import Path

import numpy as np


SAMPLE_RATE = 44_100
DURATION_SECONDS = 96.0


def quantized_frequency(frequency: float) -> float:
    """Keep every oscillator phase-continuous across the loop boundary."""
    return round(frequency * DURATION_SECONDS) / DURATION_SECONDS


def midi_frequency(note: int) -> float:
    return 440.0 * 2.0 ** ((note - 69) / 12.0)


def sine(
    time: np.ndarray,
    frequency: float,
    phase: float = 0.0,
    drift_cycles: int = 0,
    drift_depth: float = 0.0,
) -> np.ndarray:
    angle = 2.0 * np.pi * quantized_frequency(frequency) * time + phase
    if drift_cycles:
        angle += drift_depth * np.sin(
            2.0 * np.pi * drift_cycles * time / DURATION_SECONDS + phase * 0.29
        )
    return np.sin(angle).astype(np.float32)


def warm_wave(time: np.ndarray, frequency: float, phase: float) -> np.ndarray:
    """A rounded synth voice with quiet upper harmonics."""
    return (
        sine(time, frequency, phase, 2, 0.014)
        + 0.19 * sine(time, frequency * 2.0, phase + 0.8, 3, 0.010)
        + 0.065 * sine(time, frequency * 3.0, phase + 1.5, 1, 0.007)
        + 0.025 * sine(time, frequency * 4.0, phase + 2.1, 4, 0.005)
    ).astype(np.float32)


def stereo_pan(signal: np.ndarray, pan: np.ndarray | float) -> np.ndarray:
    angle = (np.asarray(pan, dtype=np.float32) + 1.0) * (np.pi / 4.0)
    return np.stack((signal * np.cos(angle), signal * np.sin(angle)), axis=1).astype(
        np.float32
    )


def harmonic_weights(time: np.ndarray, count: int) -> np.ndarray:
    position = time / DURATION_SECONDS * count
    weights = []
    for index in range(count):
        distance = np.abs(position - index)
        distance = np.minimum(distance, count - distance)
        weight = np.where(
            distance < 1.0,
            0.5 + 0.5 * np.cos(np.pi * distance),
            0.0,
        )
        weights.append(weight.astype(np.float32))
    result = np.stack(weights)
    result /= np.maximum(result.sum(axis=0, keepdims=True), 1e-8)
    return result


def elapsed_from(time: np.ndarray, event_time: float) -> np.ndarray:
    return np.mod(time - event_time, DURATION_SECONDS)


def swell_envelope(
    time: np.ndarray, event_time: float, attack: float, decay: float
) -> np.ndarray:
    elapsed = elapsed_from(time, event_time)
    return (
        (1.0 - np.exp(-elapsed / attack)) * np.exp(-elapsed / decay)
    ).astype(np.float32)


# Four long harmonic fields: Dm9, Bbmaj9, Fmaj9/A, C6/9.
CHORDS = (
    (38, (50, 53, 57, 60, 64)),
    (34, (46, 53, 57, 62, 65)),
    (33, (45, 48, 53, 57, 64)),
    (36, (48, 55, 57, 62, 64)),
)


def build_pad(time: np.ndarray, weights: np.ndarray) -> np.ndarray:
    result = np.zeros((time.size, 2), dtype=np.float32)
    voice_pans = (-0.42, 0.30, -0.18, 0.44, 0.08)
    voice_levels = (0.34, 0.28, 0.23, 0.17, 0.12)

    for chord_index, (_, notes) in enumerate(CHORDS):
        for voice_index, note in enumerate(notes):
            phase = chord_index * 0.47 + voice_index * 0.83
            tone = warm_wave(time, midi_frequency(note), phase)
            breathing = (
                0.82
                + 0.13
                * np.sin(
                    2.0
                    * np.pi
                    * (voice_index + 1)
                    * time
                    / DURATION_SECONDS
                    + phase
                )
            ).astype(np.float32)
            pan = voice_pans[voice_index] + 0.08 * np.sin(
                2.0 * np.pi * time / DURATION_SECONDS + phase
            )
            voice = voice_levels[voice_index] * weights[chord_index] * tone * breathing
            result += stereo_pan(0.31 * voice, pan)
    return result


def build_bass(time: np.ndarray, weights: np.ndarray) -> np.ndarray:
    result = np.zeros_like(time, dtype=np.float32)
    for index, (root, _) in enumerate(CHORDS):
        frequency = midi_frequency(root)
        voice = sine(time, frequency, phase=index * 0.5, drift_cycles=1, drift_depth=0.008)
        voice += 0.11 * sine(time, frequency * 2.0, phase=1.0 + index * 0.3)
        result += weights[index] * voice
    breath = (
        0.78 + 0.16 * np.sin(2.0 * np.pi * 4.0 * time / DURATION_SECONDS - 0.7)
    ).astype(np.float32)
    return stereo_pan(0.15 * result * breath, -0.03)


def build_keys(time: np.ndarray) -> np.ndarray:
    """Widely spaced electric-key notes with long synthesized tails."""
    events = (
        (5.0, 64, -0.30, 0.78),
        (14.5, 60, 0.20, 0.58),
        (29.0, 65, 0.34, 0.72),
        (39.5, 62, -0.16, 0.52),
        (53.0, 64, -0.36, 0.70),
        (63.0, 60, 0.26, 0.50),
        (77.0, 62, 0.38, 0.66),
        (88.5, 57, -0.12, 0.48),
    )
    result = np.zeros((time.size, 2), dtype=np.float32)
    for index, (event_time, note, pan, strength) in enumerate(events):
        frequency = midi_frequency(note)
        envelope = swell_envelope(time, event_time, attack=0.045, decay=5.8)
        tone = warm_wave(time, frequency, phase=0.41 * index)
        tone += 0.09 * sine(time, frequency * 4.01, phase=1.1 + index * 0.5)
        result += stereo_pan(0.035 * strength * tone * envelope, pan)
    return result


def build_distant_line(time: np.ndarray) -> np.ndarray:
    """Four slow answering tones—melody as weather, not a lead instrument."""
    events = (
        (17.0, 69, -0.44, 0.90),
        (41.0, 67, 0.36, 0.70),
        (65.0, 65, -0.20, 0.82),
        (89.0, 64, 0.46, 0.64),
    )
    result = np.zeros((time.size, 2), dtype=np.float32)
    for index, (event_time, note, pan, strength) in enumerate(events):
        frequency = midi_frequency(note)
        envelope = swell_envelope(time, event_time, attack=1.2, decay=9.5)
        tone = sine(time, frequency, phase=0.9 * index, drift_cycles=2, drift_depth=0.021)
        tone += 0.14 * sine(time, frequency * 2.0, phase=1.7 + index)
        result += stereo_pan(0.028 * strength * tone * envelope, pan)
    return result


def build_high_haze(time: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """A pitched upper halo that supplies air without using noise."""
    notes = (76, 77, 76, 74)
    result = np.zeros((time.size, 2), dtype=np.float32)
    for index, note in enumerate(notes):
        frequency = midi_frequency(note)
        tone = sine(time, frequency, phase=index * 0.7, drift_cycles=index + 1, drift_depth=0.026)
        tone += 0.12 * sine(time, frequency * 1.5, phase=1.2 + index * 0.4)
        pan = (-0.32, 0.28, -0.12, 0.38)[index]
        result += stereo_pan(0.012 * weights[index] * tone, pan)
    return result


def build_stack_resonance(time: np.ndarray) -> np.ndarray:
    """Low periodic harmonics imply distant infrastructure without percussion."""
    resonance = (
        sine(time, 55.0, 0.3, drift_cycles=2, drift_depth=0.010)
        + 0.24 * sine(time, 110.0, 1.2, drift_cycles=3, drift_depth=0.008)
        + 0.07 * sine(time, 220.0, 2.0, drift_cycles=1, drift_depth=0.006)
    )
    envelope = (
        0.47
        + 0.21 * np.sin(2.0 * np.pi * 3.0 * time / DURATION_SECONDS + 0.6)
        + 0.10 * np.sin(2.0 * np.pi * 7.0 * time / DURATION_SECONDS - 1.1)
    ).astype(np.float32)
    pan = 0.10 * np.sin(2.0 * np.pi * time / DURATION_SECONDS)
    return stereo_pan(0.023 * resonance * envelope, pan)


def write_wav(path: Path, audio: np.ndarray) -> None:
    pcm = (np.clip(audio, -1.0, 1.0) * 32_767.0).astype("<i2")
    with wave.open(str(path), "wb") as output:
        output.setnchannels(2)
        output.setsampwidth(2)
        output.setframerate(SAMPLE_RATE)
        output.writeframes(pcm.tobytes())


def render(output_directory: Path, stems: bool = False) -> tuple[Path, Path | None]:
    output_directory.mkdir(parents=True, exist_ok=True)
    sample_count = int(SAMPLE_RATE * DURATION_SECONDS)
    time = np.arange(sample_count, dtype=np.float32) / SAMPLE_RATE
    weights = harmonic_weights(time, len(CHORDS))

    layers = {
        "sustained_pad": build_pad(time, weights),
        "warm_bass": build_bass(time, weights),
        "sparse_keys": build_keys(time),
        "distant_line": build_distant_line(time),
        "high_haze": build_high_haze(time, weights),
        "stack_resonance": build_stack_resonance(time),
    }
    mix = sum(layers.values())
    mix -= np.mean(mix, axis=0, keepdims=True)
    mix = np.tanh(mix * 1.09).astype(np.float32)
    mix *= 0.47 / max(float(np.max(np.abs(mix))), 1e-8)

    wav_path = output_directory / "stack-field-rainline-ambient-music-loop.wav"
    write_wav(wav_path, mix)

    if stems:
        stem_directory = output_directory / "rainline-stems"
        stem_directory.mkdir(exist_ok=True)
        for name, layer in layers.items():
            peak = max(float(np.max(np.abs(layer))), 1e-8)
            write_wav(stem_directory / f"{name}.wav", layer * 0.76 / peak)

    mp3_path = output_directory / "stack-field-rainline-ambient-music-loop.mp3"
    try:
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-loglevel",
                "error",
                "-i",
                str(wav_path),
                "-codec:a",
                "libmp3lame",
                "-b:a",
                "256k",
                str(mp3_path),
            ],
            check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        mp3_path = None

    seam = np.abs(mix[0] - mix[-1])
    print(f"Rendered: {wav_path}")
    if mp3_path:
        print(f"Rendered: {mp3_path}")
    print(f"Seam delta (L/R): {seam[0]:.6f} / {seam[1]:.6f}")
    return wav_path, mp3_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-directory",
        type=Path,
        default=Path(__file__).resolve().parent,
    )
    parser.add_argument("--stems", action="store_true")
    args = parser.parse_args()
    render(args.output_directory, stems=args.stems)


if __name__ == "__main__":
    main()
