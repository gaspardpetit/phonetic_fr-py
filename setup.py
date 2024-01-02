from setuptools import setup, find_packages

setup(
    name='phonetic-fr',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'phonetic-fr = src.__main__:main',
        ],
    },
)
