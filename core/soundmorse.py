import wave
import struct
from pathlib import Path
import importlib.resources as pkg_resources
import core 

class soundmorse:
    def __init__(self):
        """
        Initialize with bundled PCM beeps (short and long)
        """
        # Read bundled PCM files
        self.short_beep = pkg_resources.read_binary('Qmorse.core.sounds', "1_short.pcm")
        self.long_beep = pkg_resources.read_binary('Qmorse.core.sounds', "1_long.pcm")
    @staticmethod
    def _append_silence(duration_sec:int, sample_rate=44100) -> bytes:
        """Generate silence for duration_sec seconds"""
        n_samples = int(duration_sec * sample_rate)
        silence = struct.pack("<" + "h"*n_samples, *([0]*n_samples))
        return silence
    
    @staticmethod
    def bimorse_to_audio(bimorse_input:str, short_beep:bytes, long_beep:bytes, output_file="output.wav", sample_rate=44100):
        """
        Convert bimorse string or file to WAV audio.
        """
        # Read bimorse content if input is a file
        path = Path(bimorse_input)
        if path.is_file():
            bimorse = ''.join(filter(lambda x: x in "01", path.read_text()))
        else:
            bimorse = ''.join(filter(lambda x: x in "01", bimorse_input))

        audio_data = bytearray()
        i = 0
        while i < len(bimorse):
            char = bimorse[i]
            if char == "0":
                audio_data.extend(short_beep)
            elif char == "1":
                audio_data.extend(long_beep)

            seq_len = 1
            j = i + 1
            while j < len(bimorse) and bimorse[j] == char:
                seq_len += 1
                j += 1

            silence_sec = seq_len + 1 if seq_len > 1 else 1
            audio_data.extend(soundmorse._append_silence(silence_sec, sample_rate))
            i += seq_len

        # Save WAV file
        with wave.open(output_file, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(4)  # 32-bit PCM
            w.setframerate(sample_rate)
            w.writeframes(audio_data)

        print(f"Saved audio to {output_file}")