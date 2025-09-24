import wave
import struct
from pathlib import Path
from importlib import resources
from typing import Optional

class soundmorse:
    """
    Convert Binary Morse (bimorse) to audio.
    0 = short beep, 1 = long beep.
    """

    def __init__(self):
        """Load bundled PCM beep sounds from the package."""
        self.short_beep = resources.files('Qmorse.sounds').joinpath("1_short.pcm").read_bytes()
        self.long_beep  = resources.files('Qmorse.sounds').joinpath("1_long.pcm").read_bytes()

    @staticmethod
    def _append_silence(duration_sec: float, sample_rate=44100) -> bytes:
        """Generate silence for given duration in seconds."""
        n_samples = int(duration_sec * sample_rate)
        # 32-bit PCM: little-endian signed integers
        silence = struct.pack("<" + "i"*n_samples, *([0]*n_samples))
        return silence

    @staticmethod
    def bimorse_to_audio(
        input: str,
        output="output.wav",
        sample_rate=44100,
    short_beep: Optional[bytes] = None,
    long_beep: Optional[bytes] = None
    ):
        """
        Static version: convert bimorse to audio.
        Will load default PCM beeps if short_beep/long_beep are not provided.
        """
        if short_beep is None or long_beep is None:
            short_beep = resources.files('Qmorse.sounds').joinpath("1_short.pcm").read_bytes()
            long_beep  = resources.files('Qmorse.sounds').joinpath("1_long.pcm").read_bytes()

        path = Path(input)
        if path.is_file():
            bimorse = ''.join(filter(lambda x: x in "01", path.read_text()))
        else:
            bimorse = ''.join(filter(lambda x: x in "01", input))

        audio_data = bytearray()
        i = 0
        while i < len(bimorse):
            char = bimorse[i]
            audio_data.extend(short_beep if char == "0" else long_beep)

            seq_len = 1
            j = i + 1
            while j < len(bimorse) and bimorse[j] == char:
                seq_len += 1
                j += 1

            silence_sec = 1 if seq_len == 1 else seq_len + 1
            audio_data.extend(soundmorse._append_silence(silence_sec, sample_rate))
            i += seq_len

        with wave.open(output, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(4)
            w.setframerate(sample_rate)
            w.writeframes(audio_data)

        print(f"Saved audio to {output}")
