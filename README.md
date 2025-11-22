# Qmorse

**Qmorse** is a lightweight Python library for working with **Binary Morse code**.  
It provides a precise, timing-aware representation of Morse that can be used for messaging systems, digital signal experiments, custom broadcasting formats, or any project where Morse must behave like an actual timed signal rather than decorative characters.

Binary Morse in Qmorse uses:

- `0` → short pulse (dot)  
- `1` → long pulse (dash)  
- `.` → silence  

This format mirrors the structure of real Morse transmissions, making it suitable for practical encoding, decoding, and transportation across different media.

---

## Features

- **Binary Morse Encoding & Decoding**  
  Convert between readable text and a strict binary-timed Morse representation.

- **Realistic Morse Timing**  
  Silence (`.`) is preserved explicitly, enabling accurate reconstruction and physical signaling.

- **File Handling**  
  Save or load `.txt` and `.bimorse` files containing binary Morse sequences.

- **Minimal & Flexible**  
  Small footprint, no external dependencies, designed for embedding into larger systems.

---

## Installation

Install from PyPI:

```bash
pip install Qmorse

Local installation:

git clone https://github.com/amiralihabibzadeh/Qmorse.git
cd Qmorse
pip install .

Usage Example

from Qmorse import bimorse as bim

text = bim.to_bimorse("Cogito, ergo sum")
bim.save_file(text, "rene.bimorse")

About

Qmorse provides the low-level binary form of Morse where timing is explicit and machine-interpretable.
This allows it to integrate naturally with optical signaling, audio pulses, embedded systems, or formats such as video-encoded Morse.