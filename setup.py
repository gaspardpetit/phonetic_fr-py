"""Setup file for building package"""
from setuptools import setup, find_packages

setup(
    name='phonetic_fr',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'phonetic_fr = phonetic_distance.__main__:main',
        ],
    },
)
