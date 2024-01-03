"""Setup file for building package"""
from pathlib import Path
import re
from setuptools import setup, find_packages

with open('phonetic_fr/__init__.py', encoding="utf-8") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

requirements = []
try:
    with open('requirements.txt', encoding="utf-8") as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    pass

setup(
    name='phonetic_fr',
    version=version,
    description="Computes phonetic representation of French words",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'phonetic_fr = phonetic_distance.__main__:main',
        ],
    },
    install_requires=requirements,
    python_requires=">=3.6",
    url="https://github.com/gaspardpetit/phonetic_fr-py",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
