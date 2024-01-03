"""Setup file for building package"""
from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='phonetic_fr',
    version='1.0',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'phonetic_fr = phonetic_distance.__main__:main',
        ],
    },
)
