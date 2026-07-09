# Usage
Run the generator directly from the terminal to create your audio file:

# Bash
#Generate a 100-note sequence
python3 main.py --count 100

The output will be saved as output.wav in your project directory.

# Technical Details
# Digital Root Calculation
The digital root is calculated recursively to ensure the output remains constrained within a musical scale (1–9). This provides a predictable, yet mathematically complex, melodic pattern that avoids dissonance.

# Waveform Synthesis
The audio engine generates periodic sine waves based on specific frequency mappings (Hz). The amplitude is modulated by a linear attack/release function:

f(t) = A(t) * sin(2πft)

Where A(t) represents the envelope function that smooths the transition at note onset and offset.

# Portfolio Note
This project demonstrates proficiency in:

# Modular Design: 
Applying software engineering principles to research-oriented code.

# Signal Processing: 
Moving from discrete mathematical models to continuous digital audio.

# Tool Development: 
Building command-line utilities for workflow automation.

