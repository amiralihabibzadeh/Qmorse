from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="Qmorse",
    version="1.1.3",
    author="Hobab",
    author_email="b66669420@gmail.com",
    description="A lightweight Morse-like encoder/decoder library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amiralihabibzadeh/Qmorse",
    packages=find_packages(include=["Qmorse", "Qmorse.*"]),
    include_package_data=True,
    package_data={
        "core": ['sounds/*.pcm']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Morse Code",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[],
    keywords="morse binary encoding decoding python",
)
