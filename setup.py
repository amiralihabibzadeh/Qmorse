from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="Qmorse",
    version="1.1.19",
    author="Hobab",
    author_email="b66669420@gmail.com",
    description="A lightweight Morse-like library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amiralihabibzadeh/Qmorse",
    packages=find_packages(include=["Qmorse", "Qmorse.*"]),
    include_package_data=True,
    install_requires=[ 
        "pydub>=0.25.1",
        "lameenc>=1.8.1",
    ],
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
    package_data={"Qmorse": ["sounds/*.pcm"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="morse binary encoding decoding python",
)
