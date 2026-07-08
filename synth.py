import numpy as np

def apply_envelope(data, sample_rate):
    """Applies a simple Attack/Release envelope to smooth audio."""
    length = len(data)
    a, r = int(length * 0.1), int(length * 0.1)
    envelope = np.ones(length)
    envelope[:a] = np.linspace(0, 1, a)
    envelope[-r:] = np.linspace(1, 0, r)
    return data * envelope

def generate_note(freq, duration, sample_rate=44100):
    """Generates a sine wave note with an envelope."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * freq * t)
    return apply_envelope(wave, sample_rate)
