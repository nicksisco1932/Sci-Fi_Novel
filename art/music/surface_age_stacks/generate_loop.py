"""Generate the original seamless ambient loop "Stack Field: Low Weather".

The composition is entirely procedural and uses no recorded or sampled material.
It is designed as an 80-second stereo loop at 48 BPM.
"""

from __future__ import annotations

import argparse
import math
import subprocess
import wave
from pathlib import Path

import numpy as np


SAMPLE_RATE = 44_100
DURATION_SECONDS = 80.0
BPM = 48.0
SEED = 27_041


def loop_frequency(frequency: float) -> float:
    """Quantize a frequency so it completes whole cycles over the loop."""
    return round(frequency * DURATION_SECONDS) / DURATION_SECONDS


def oscillator(
    time: np.ndarray,
    frequency: float,
    phase: float = 0.0,
    lfo_cycles: int = 0,
    lfo_depth: float = 0.0,
) -> np.ndarray:
    frequency = loop_frequency(frequency)
    angle = 2.0 * np.pi * frequency * time + phase
    if lfo_cycles:
        angle += lfo_depth * np.sin(
            2.0 * np.pi * lfo_cycles * time / DURATION_SECONDS + phase * 0.37
        )
    return np.sin(angle).astype(np.float32)


def circular_chord_weights(time: np.ndarray, chord_count: int = 4) -> np.ndarray:
    """Make raised-cosine chord weights whose beginning and end join exactly."""
    position = time / DURATION_SECONDS * chord_count
    weights = []
    for index in range(chord_count):
        distance = np.abs(position - index)
        distance = np.minimum(distance, chord_count - distance)
        weight = np.where(
            distance < 1.0,
            0.5 + 0.5 * np.cos(np.pi * distance),
            0.0,
        )
        weights.append(weight.astype(np.float32))
    result = np.stack(weights)
    result /= np.maximum(result.sum(axis=0, keepdims=True), 1e-8)
    return result


def stereo_pan(signal: np.ndarray, pan: np.ndarray | float) -> np.ndarray:
    """Equal-power pan a mono signal; -1 is left and +1 is right."""
    angle = (np.asarray(pan, dtype=np.float32) + 1.0) * (np.pi / 4.0)
    left = signal * np.cos(angle)
    right = signal * np.sin(angle)
    return np.stack((left, right), axis=1).astype(np.float32)


def spectral_noise(
    sample_count: int,
    rng: np.random.Generator,
    low_cut: float,
    high_cut: float,
    slope: float,
) -> np.ndarray:
    """Create periodic, spectrally shaped noise using an inverse real FFT."""
    frequencies = np.fft.rfftfreq(sample_count, 1.0 / SAMPLE_RATE)
    phases = rng.uniform(0.0, 2.0 * np.pi, frequencies.size)
    magnitude = 1.0 / np.power(np.maximum(frequencies, 0.05), slope)
    if low_cut > 0.0:
        magnitude *= 1.0 - np.exp(-np.square(frequencies / low_cut))
    magnitude *= np.exp(-np.power(frequencies / high_cut, 2.0))
    magnitude[0] = 0.0
    spectrum = magnitude * np.exp(1j * phases)
    noise = np.fft.irfft(spectrum, n=sample_count).astype(np.float32)
    noise /= max(float(np.std(noise)), 1e-8)
    return noise


def build_weather(
    time: np.ndarray, sample_count: int, rng: np.random.Generator
) -> np.ndarray:
    low = spectral_noise(sample_count, rng, 0.08, 420.0, 0.82)
    air = spectral_noise(sample_count, rng, 90.0, 3_200.0, 0.36)
    side = spectral_noise(sample_count, rng, 0.12, 1_100.0, 0.67)

    storm_breath = (
        0.72
        + 0.15 * np.sin(2.0 * np.pi * 3.0 * time / DURATION_SECONDS + 0.4)
        + 0.09 * np.sin(2.0 * np.pi * 7.0 * time / DURATION_SECONDS + 2.1)
    ).astype(np.float32)
    left = (0.115 * low + 0.025 * air + 0.022 * side) * storm_breath
    right = (0.115 * low + 0.025 * air - 0.022 * side) * storm_breath

    # Broad low thunder without a literal thunderclap.
    shelf = np.zeros_like(time, dtype=np.float32)
    for center, strength, width in ((31.0, 0.7, 7.0), (56.0, 1.0, 9.0)):
        distance = np.minimum(
            np.abs(time - center), DURATION_SECONDS - np.abs(time - center)
        )
        shelf += strength * np.exp(-0.5 * np.square(distance / width)).astype(np.float32)
    rumble = oscillator(time, 29.0, phase=1.2, lfo_cycles=2, lfo_depth=0.06)
    weather = np.stack((left, right), axis=1)
    weather += stereo_pan(0.032 * rumble * shelf, -0.18)
    return weather.astype(np.float32)


def build_structure(time: np.ndarray) -> np.ndarray:
    weights = circular_chord_weights(time)
    # Dm(add9) -> Bbmaj7 -> Fmaj7/A -> C(add9), voiced as distant mass.
    chords = (
        (36.71, 73.42, 110.00, 146.83, 164.81),
        (29.14, 58.27, 87.31, 116.54, 146.83),
        (27.50, 55.00, 87.31, 110.00, 130.81),
        (32.70, 65.41, 98.00, 130.81, 146.83),
    )
    chord_signals = []
    for chord_index, chord in enumerate(chords):
        tone = np.zeros_like(time, dtype=np.float32)
        for voice_index, frequency in enumerate(chord):
            amplitude = (0.50, 0.34, 0.24, 0.17, 0.12)[voice_index]
            phase = 0.41 * chord_index + 0.73 * voice_index
            tone += amplitude * oscillator(
                time,
                frequency,
                phase=phase,
                lfo_cycles=voice_index + 1,
                lfo_depth=0.012 + 0.004 * voice_index,
            )
        chord_signals.append(tone)

    pad = sum(weights[index] * chord_signals[index] for index in range(4))
    slow_pan = 0.18 * np.sin(2.0 * np.pi * time / DURATION_SECONDS - 0.8)
    structure = stereo_pan(0.155 * pad, slow_pan)

    # A narrow, almost subliminal resonance gives the stacks their vertical scale.
    high_resonance = (
        0.55 * oscillator(time, 220.0, 0.2, lfo_cycles=3, lfo_depth=0.018)
        + 0.28 * oscillator(time, 329.63, 1.1, lfo_cycles=2, lfo_depth=0.013)
    )
    resonance_envelope = (
        0.5
        + 0.5 * np.sin(2.0 * np.pi * 2.0 * time / DURATION_SECONDS - 1.1)
    ).astype(np.float32)
    structure += stereo_pan(0.019 * high_resonance * resonance_envelope, 0.24)
    return structure.astype(np.float32)


def build_machinery(time: np.ndarray) -> np.ndarray:
    beat_seconds = 60.0 / BPM
    cycle_seconds = beat_seconds * 2.0
    cycle = np.mod(time, cycle_seconds)
    pulse_index = np.floor(time / cycle_seconds).astype(np.int32)
    pattern = np.asarray(
        [0.72, 0.48, 0.62, 0.40, 0.70, 0.52, 0.58, 0.34] * 4,
        dtype=np.float32,
    )
    envelope = (1.0 - np.exp(-cycle / 0.045)) * np.exp(-cycle / 0.62)
    envelope *= pattern[pulse_index % pattern.size]
    sub = (
        oscillator(time, 36.71, phase=-0.4)
        + 0.23 * oscillator(time, 73.42, phase=0.7)
    )
    machinery = stereo_pan(0.080 * sub * envelope, -0.08)

    # A slow pressure-release rhythm every two bars.
    long_cycle = np.mod(time + 0.6, 10.0)
    release_envelope = (
        (1.0 - np.exp(-long_cycle / 0.22)) * np.exp(-long_cycle / 2.4)
    ).astype(np.float32)
    release = (
        oscillator(time, 98.0, 1.8, lfo_cycles=4, lfo_depth=0.025)
        + 0.35 * oscillator(time, 196.0, 0.9, lfo_cycles=4, lfo_depth=0.018)
    )
    release_pan = 0.42 * np.sin(2.0 * np.pi * time / 40.0)
    machinery += stereo_pan(0.021 * release * release_envelope, release_pan)
    return machinery.astype(np.float32)


def circular_decay(time: np.ndarray, event_time: float, decay: float) -> np.ndarray:
    elapsed = np.mod(time - event_time, DURATION_SECONDS)
    return (
        (1.0 - np.exp(-elapsed / 0.08)) * np.exp(-elapsed / decay)
    ).astype(np.float32)


def build_signals(time: np.ndarray) -> np.ndarray:
    events = (
        (7.5, 659.25, -0.46, 0.85),
        (26.25, 440.00, 0.34, 0.62),
        (47.5, 587.33, -0.18, 0.74),
        (66.25, 523.25, 0.52, 0.55),
    )
    result = np.zeros((time.size, 2), dtype=np.float32)
    for index, (event_time, frequency, pan, strength) in enumerate(events):
        envelope = circular_decay(time, event_time, decay=5.2 + index * 0.35)
        bell = (
            oscillator(time, frequency, phase=0.3 * index)
            + 0.33 * oscillator(time, frequency * 2.01, phase=1.4 + index)
            + 0.12 * oscillator(time, frequency * 3.98, phase=2.1 - index * 0.2)
        )
        result += stereo_pan(0.020 * strength * bell * envelope, pan)
    return result


def build_horizon(time: np.ndarray) -> np.ndarray:
    # Warmth peaks opposite the heaviest weather and recedes without disappearing.
    warmth = (
        0.36
        + 0.32 * np.cos(2.0 * np.pi * (time - 9.0) / DURATION_SECONDS)
        + 0.12 * np.cos(4.0 * np.pi * (time - 13.0) / DURATION_SECONDS)
    )
    warmth = np.clip(warmth, 0.04, 0.86).astype(np.float32)
    tone = (
        0.62 * oscillator(time, 293.66, 0.8, lfo_cycles=1, lfo_depth=0.018)
        + 0.38 * oscillator(time, 369.99, 1.7, lfo_cycles=2, lfo_depth=0.014)
        + 0.23 * oscillator(time, 440.00, 2.2, lfo_cycles=3, lfo_depth=0.011)
    )
    pan = -0.28 + 0.14 * np.sin(2.0 * np.pi * time / DURATION_SECONDS)
    return stereo_pan(0.026 * tone * warmth, pan)


def write_pcm16_wav(path: Path, audio: np.ndarray) -> None:
    pcm = np.clip(audio, -1.0, 1.0)
    pcm = (pcm * 32_767.0).astype("<i2")
    with wave.open(str(path), "wb") as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)
        wav.writeframes(pcm.tobytes())


def render(output_directory: Path, export_stems: bool = False) -> tuple[Path, Path | None]:
    output_directory.mkdir(parents=True, exist_ok=True)
    sample_count = int(SAMPLE_RATE * DURATION_SECONDS)
    time = np.arange(sample_count, dtype=np.float32) / SAMPLE_RATE
    rng = np.random.default_rng(SEED)

    layers = {
        "weather": build_weather(time, sample_count, rng),
        "structure": build_structure(time),
        "machinery": build_machinery(time),
        "signals": build_signals(time),
        "horizon": build_horizon(time),
    }

    mix = sum(layers.values())
    mix -= np.mean(mix, axis=0, keepdims=True)
    mix = np.tanh(mix * 1.28).astype(np.float32)
    peak = float(np.max(np.abs(mix)))
    mix *= 0.89 / max(peak, 1e-8)

    wav_path = output_directory / "stack-field-low-weather-loop.wav"
    write_pcm16_wav(wav_path, mix)

    if export_stems:
        stem_directory = output_directory / "stems"
        stem_directory.mkdir(exist_ok=True)
        for name, audio in layers.items():
            stem_peak = float(np.max(np.abs(audio)))
            write_pcm16_wav(stem_directory / f"{name}.wav", audio * (0.82 / stem_peak))

    mp3_path = output_directory / "stack-field-low-weather-loop.mp3"
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

    # Report the join discontinuity for quick technical QA.
    seam_delta = np.abs(mix[0] - mix[-1])
    print(f"Rendered: {wav_path}")
    if mp3_path:
        print(f"Rendered: {mp3_path}")
    print(
        "Seam delta (L/R): "
        f"{seam_delta[0]:.6f} / {seam_delta[1]:.6f}; peak: {peak:.6f}"
    )
    return wav_path, mp3_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-directory",
        type=Path,
        default=Path(__file__).resolve().parent,
    )
    parser.add_argument("--stems", action="store_true", help="Also export layer stems.")
    args = parser.parse_args()
    render(args.output_directory, export_stems=args.stems)


if __name__ == "__main__":
    main()
