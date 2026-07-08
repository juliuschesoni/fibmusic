import numpy as np
from scipy.io import wavfile
import argparse
from synth import generate_note

def get_fibonacci_sequence(count):
    fib = [1, 1, 2]
    while len(fib) < count:
        fib.append(2 * fib[-1] - fib[-3])
    # Digital root logic
    return [sum(int(d) for d in str(n)) % 9 + 1 for n in fib]

def main():
    parser = argparse.ArgumentParser(description="Generate math-based music.")
    parser.add_argument("--count", type=int, default=50, help="Number of notes")
    args = parser.parse_args()

    # Mapping 1-9 to C Major frequencies
    freqs = {1: 261.63, 2: 293.66, 3: 329.63, 4: 349.23, 5: 392.00, 6: 440.00, 7: 493.88, 8: 523.25, 9: 587.33}
    
    roots = get_fibonacci_sequence(args.count)
    audio_data = np.concatenate([generate_note(freqs[r], 0.5) for r in roots])

    wavfile.write("output.wav", 44100, (audio_data * 32767).astype(np.int16))
    print(f"Generated {args.count} notes to output.wav")

if __name__ == "__main__":
    main()
