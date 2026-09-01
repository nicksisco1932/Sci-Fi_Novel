"""Generate "Stack Field: Afterlight", a seamless music-forward ambient loop.

No samples are used. The arrangement is synthesized from pads, bass, keys,
arpeggios, tonal percussion, and a very quiet harmonic atmosphere.
"""

from __future__ import annotations

import argparse
import subprocess
import wave
from pathlib import Path

import numpy as np


SAMPLE_RATE = 44_100
DURATION_SECONDS = 80.0
BPM = 48.0
BEAT_SECONDS = 60.0 / BPM
BAR_SECONDS = BEAT_SECONDS * 4.0


def loop_frequency(frequency: float) -> float:
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
    angle = 2.0 * np.pi * loop_frequency(frequency) * time + phase
    if drift_cycles:
        angle += drift_depth * np.sin(
            2.0 * np.pi * drift_cycles * time / DURATION_SECONDS + phase * 0.31
        )
    return np.sin(angle).astype(np.float32)


def soft_tone(time: np.ndarray, frequency: float, phase: float = 0.0) -> np.ndarray:
    fundamental = sine(time, frequency, phase, drift_cycles=2, drift_depth=0.009)
    second = sine(time, frequency * 2.0, phase + 0.7, drift_cycles=3, drift_depth=0.007)
    third = sine(time, frequency * 3.0, phase + 1.4, drift_cycles=1, drift_depth=0.005)
    return (fundamental + 0.16 * second + 0.045 * third).astype(np.float32)


def stereo_pan(signal: np.ndarray, pan: np.ndarray | float) -> np.ndarray:
    angle = (np.asarray(pan, dtype=np.float32) + 1.0) * (np.pi / 4.0)
    return np.stack((signal * np.cos(angle), signal * np.sin(angle)), axis=1).astype(
        np.float32
    )


def slot_weights(time: np.ndarray, slot_count: int) -> np.ndarray:
    """Periodic crossfades centered on each harmonic slot."""
    position = time / DURATION_SECONDS * slot_count
    result = []
    for index in range(slot_count):
        distance = np.abs(position - index)
        distance = np.minimum(distance, slot_count - distance)
        weight = np.where(
            distance < 1.0,
            0.5 + 0.5 * np.cos(np.pi * distance),
            0.0,
        )
        result.append(weight.astype(np.float32))
    weights = np.stack(result)
    weights /= np.maximum(weights.sum(axis=0, keepdims=True), 1e-8)
    return weights


def circular_elapsed(time: np.ndarray, event_time: float) -> np.ndarray:
    return np.mod(time - event_time, DURATION_SECONDS)


def pluck_envelope(
    time: np.ndarray, event_time: float, attack: float, decay: float
) -> np.ndarray:
    elapsed = circular_elapsed(time, event_time)
    return (
        (1.0 - np.exp(-elapsed / attack)) * np.exp(-elapsed / decay)
    ).astype(np.float32)


# Two bars per chord. The final suspended A turns naturally back into D minor.
CHORDS = (
    (38, (50, 53, 57, 60, 64)),  # Dm9
    (34, (46, 53, 57, 62, 65)),  # Bbmaj9
    (33, (45, 48, 53, 57, 64)),  # Fmaj7/A
    (36, (48, 55, 60, 62, 64)),  # Cadd9
    (38, (50, 53, 57, 60, 64)),  # Dm9
    (34, (46, 53, 57, 62, 65)),  # Bbmaj9
    (31, (43, 50, 53, 57, 62)),  # Gm9
    (33, (45, 52, 57, 62, 64)),  # Asus4(add9)
)


def build_pad(time: np.ndarray, weights: np.ndarray) -> np.ndarray:
    voices = []
    for chord_index, (_, notes) in enumerate(CHORDS):
        chord = np.zeros_like(time, dtype=np.float32)
        for voice_index, note in enumerate(notes):
            amplitude = (0.38, 0.29, 0.24, 0.18, 0.13)[voice_index]
            chord += amplitude * soft_tone(
                time,
                midi_frequency(note),
                phase=0.53 * chord_index + 0.81 * voice_index,
            )
        voices.append(chord)
    pad = sum(weights[index] * voices[index] for index in range(len(CHORDS)))
    movement = 0.03 * np.sin(2.0 * np.pi * time / DURATION_SECONDS - 0.4)
    return stereo_pan(0.255 * pad, movement)


def build_bass(time: np.ndarray, weights: np.ndarray) -> np.ndarray:
    bass = np.zeros_like(time, dtype=np.float32)
    for index, (root, _) in enumerate(CHORDS):
        frequency = midi_frequency(root)
        voice = sine(time, frequency, phase=0.3 * index)
        voice += 0.13 * sine(time, frequency * 2.0, phase=1.1 + index * 0.2)
        bass += weights[index] * voice

    # Sidechain-like breathing gives motion without turning into a club beat.
    beat_phase = np.mod(time, BEAT_SECONDS)
    breath = 0.72 + 0.28 * (1.0 - np.exp(-beat_phase / 0.34))
    return stereo_pan(0.175 * bass * breath, -0.04)


def build_keys(time: np.ndarray) -> np.ndarray:
    result = np.zeros((time.size, 2), dtype=np.float32)
    # Three notes per bar: recognizable phrasing with deliberate empty space.
    beat_pattern = (0.0, 1.5, 3.0)
    note_pattern = (4, 2, 3, 1, 4, 3, 2, 1)
    for bar in range(16):
        chord_index = bar // 2
        notes = CHORDS[chord_index][1]
        for event_index, beat in enumerate(beat_pattern):
            event_time = bar * BAR_SECONDS + beat * BEAT_SECONDS
            note_index = note_pattern[(bar + event_index) % len(note_pattern)]
            note = notes[note_index] + 12
            frequency = midi_frequency(note)
            envelope = pluck_envelope(time, event_time, attack=0.035, decay=2.4)
            tone = soft_tone(time, frequency, phase=0.37 * bar + event_index)
            tone += 0.10 * sine(time, frequency * 4.0, phase=1.7 + event_index)
            pan = (-0.28, 0.22, -0.05)[event_index]
            result += stereo_pan(0.034 * tone * envelope, pan)
    return result


def build_arpeggio(time: np.ndarray) -> np.ndarray:
    result = np.zeros((time.size, 2), dtype=np.float32)
    step_pattern = (0, 2, 1, 3, 2, 4, 3, 1)
    step_seconds = BEAT_SECONDS / 2.0
    for step in range(128):
        event_time = step * step_seconds
        bar = step // 8
        chord_index = bar // 2
        notes = CHORDS[chord_index][1]
        note = notes[step_pattern[step % 8]] + 12
        frequency = midi_frequency(note)
        envelope = pluck_envelope(time, event_time, attack=0.018, decay=0.62)
        tone = sine(time, frequency, phase=0.19 * step)
        tone += 0.09 * sine(time, frequency * 2.0, phase=1.0 + 0.13 * step)
        pan = 0.34 * np.sin(2.0 * np.pi * step / 32.0)
        result += stereo_pan(0.0135 * tone * envelope, pan)
    return result


def build_pulse(time: np.ndarray) -> np.ndarray:
    result = np.zeros((time.size, 2), dtype=np.float32)
    # Soft sine percussion on beats one and three.
    for bar in range(16):
        for beat, strength in ((0.0, 1.0), (2.0, 0.58)):
            event_time = bar * BAR_SECONDS + beat * BEAT_SECONDS
            elapsed = circular_elapsed(time, event_time)
            envelope = (1.0 - np.exp(-elapsed / 0.012)) * np.exp(-elapsed / 0.34)
            phase = 2.0 * np.pi * (
                43.0 * elapsed + 18.0 * 0.055 * (1.0 - np.exp(-elapsed / 0.055))
            )
            kick = np.sin(phase).astype(np.float32)
            result += stereo_pan(0.095 * strength * kick * envelope, -0.06)

        # Tonal rim on beat four; no noise component.
        event_time = bar * BAR_SECONDS + 3.0 * BEAT_SECONDS
        envelope = pluck_envelope(time, event_time, attack=0.006, decay=0.11)
        rim = sine(time, 920.0, phase=bar * 0.2) + 0.28 * sine(
            time, 1_640.0, phase=1.3 + bar * 0.1
        )
        result += stereo_pan(0.011 * rim * envelope, 0.16)
    return result


def build_horizon(time: np.ndarray) -> np.ndarray:
    # A restrained melodic answer appears once per four bars.
    result = np.zeros((time.size, 2), dtype=np.float32)
    events = (
        (17.5, 69, -0.42),
        (37.5, 67, 0.36),
        (57.5, 65, -0.18),
        (77.5, 64, 0.44),
    )
    for index, (event_time, note, pan) in enumerate(events):
        envelope = pluck_envelope(time, event_time, attack=0.18, decay=5.8)
        frequency = midi_frequency(note)
        tone = sine(time, frequency, phase=index * 0.8, drift_cycles=2, drift_depth=0.014)
        tone += 0.20 * sine(time, frequency * 2.0, phase=1.2 + index)
        result += stereo_pan(0.023 * tone * envelope, pan)
    return result


def build_tonal_air(time: np.ndarray) -> np.ndarray:
    """Quiet pitched atmosphere—not broadband static or wind noise."""
    air = (
        0.52 * sine(time, midi_frequency(74), 0.4, drift_cycles=3, drift_depth=0.025)
        + 0.31 * sine(time, midi_frequency(81), 1.2, drift_cycles=4, drift_depth=0.019)
        + 0.17 * sine(time, midi_frequency(86), 2.0, drift_cycles=5, drift_depth=0.016)
    )
    envelope = (
        0.45
        + 0.25 * np.cos(2.0 * np.pi * (time - 8.0) / DURATION_SECONDS)
        + 0.08 * np.sin(6.0 * np.pi * time / DURATION_SECONDS)
    ).astype(np.float32)
    pan = -0.20 + 0.40 * time / DURATION_SECONDS
    return stereo_pan(0.009 * air * envelope, pan)


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
    weights = slot_weights(time, len(CHORDS))

    layers = {
        "pad": build_pad(time, weights),
        "bass": build_bass(time, weights),
        "keys": build_keys(time),
        "arpeggio": build_arpeggio(time),
        "pulse": build_pulse(time),
        "horizon_melody": build_horizon(time),
        "tonal_air": build_tonal_air(time),
    }
    mix = sum(layers.values())
    mix -= np.mean(mix, axis=0, keepdims=True)
    mix = np.tanh(mix * 1.18).astype(np.float32)
    # Leave listening-room headroom; this is background music, not a loudness master.
    mix *= 0.56 / max(float(np.max(np.abs(mix))), 1e-8)

    wav_path = output_directory / "stack-field-afterlight-music-loop.wav"
    write_wav(wav_path, mix)

    if stems:
        stem_directory = output_directory / "music-stems"
        stem_directory.mkdir(exist_ok=True)
        for name, layer in layers.items():
            peak = max(float(np.max(np.abs(layer))), 1e-8)
            write_wav(stem_directory / f"{name}.wav", layer * 0.82 / peak)

    mp3_path = output_directory / "stack-field-afterlight-music-loop.mp3"
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
