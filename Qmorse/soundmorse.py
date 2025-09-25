import wave
from pathlib import Path
from importlib import resources
import lameenc  

class soundmorse:
    short_beep = resources.files('Qmorse.sounds').joinpath("1_short.pcm").read_bytes()
    long_beep  = resources.files('Qmorse.sounds').joinpath("1_long.pcm").read_bytes()

    @staticmethod
    def _append_silence(duration_sec: float, sample_rate: int) -> bytes:
        num_samples = int(duration_sec * sample_rate)
        return b'\x00\x00\x00\x00' * num_samples  

    @staticmethod
    def _get_silence_duration(seq_len: int) -> float:
        return {1: 0.5, 2: 1.0, 3: 1.5}.get(seq_len, 2.0)

    @staticmethod
    def bimorse_to_audio(input: str, output="output.wav", sample_rate=44100):

        path = Path(input)
        if path.is_file():
            bimorse = ''.join(filter(lambda x: x in "01", path.read_text()))
        else:
            bimorse = ''.join(filter(lambda x: x in "01", input))

        audio_data = bytearray()
        i = 0
        while i < len(bimorse):
            char = bimorse[i]
            audio_data.extend(soundmorse.short_beep if char == "0" else soundmorse.long_beep)

            seq_len = 1
            j = i + 1
            while j < len(bimorse) and bimorse[j] == char:
                seq_len += 1
                j += 1

            silence_sec = soundmorse._get_silence_duration(seq_len)
            audio_data.extend(soundmorse._append_silence(silence_sec, sample_rate))
            i += seq_len

        output_path = Path(output)
        ext = output_path.suffix.lower().replace('.', '')

        if ext == "wav":
            with wave.open(str(output_path), "wb") as w:
                w.setnchannels(1)
                w.setsampwidth(4) 
                w.setframerate(sample_rate)
                w.writeframes(audio_data)
        elif ext == "mp3":
            encoder = lameenc.Encoder()
            encoder.set_bit_rate(192)
            encoder.set_in_sample_rate(sample_rate)
            encoder.set_channels(1)
            encoder.set_quality(2) 

            mp3_data = encoder.encode(bytes(audio_data))
            mp3_data += encoder.flush()

            with open(output_path, "wb") as f:
                f.write(mp3_data)
        else:
            raise ValueError("Unsupported format. Only WAV and MP3 are allowed.")

        print(f"Saved audio to {output_path}")
