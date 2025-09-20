from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="Qmorse",
    version="1.0.0",
    author="Hobab",
    author_email="b66669420@gmail.com",
    description="A mini library for encoding and decoding Binary Morse code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amiralihabibzadeh/Qmorse",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
