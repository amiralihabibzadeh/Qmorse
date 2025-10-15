from pydub import AudioSegment as AS
from importlib import resources

class SoundMorse:
    # Load short and long sounds from package
    with resources.files("Qmorse.sounds").joinpath("short.mp3").open("rb") as f:
        short = AS.from_file(f, format="mp3")

    with resources.files("Qmorse.sounds").joinpath("long.mp3").open("rb") as f:
        long = AS.from_file(f, format="mp3")

    silence = AS.silent(duration=500)

    @staticmethod
    def reader(input_str: str) -> list:

        """Convert a string of 0s/1s into a sequence of AudioSegments."""

        Combine = []
        for i in input_str:
            Combine.append(SoundMorse.silence)
            if i == '0':
                Combine.append(SoundMorse.short)
            elif i == '1':
                Combine.append(SoundMorse.long)
            else:
                Combine.append(SoundMorse.silence)
    
        return Combine

    @staticmethod
    def bimorse_to_audio(input_str: str, output="Bimorse.mp3") -> None:

        """Generate combined Morse-like sound sequence and export it."""

        segments = SoundMorse.reader(input_str)
        combined = AS.silent(duration=0)
        for seg in segments:
            combined += seg
        combined.export(output, format="mp3")
        print(f"✅ File created successfully: {output}")
