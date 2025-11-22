from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="Qmorse",
    version="2.0.1",
    author="Hobab",
    author_email="b66669420@gmail.com",
    description="Binary Morse encoding and decoding for real-world signal use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amiralihabibzadeh/Qmorse",

    packages=find_packages(include=["Qmorse", "Qmorse.*"]),
    include_package_data=True,

    python_requires=">=3.7",
    keywords="morse binary encoding decoding signal communication",

    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=24.0.0",
            "ruff>=0.5.0",
            "setuptools>=61.0.0",
            "wheel>=0.37.0",
            "twine>=4.0.0",
        ],
    },
)
