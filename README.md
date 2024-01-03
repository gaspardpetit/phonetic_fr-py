[![PyPI version](https://badge.fury.io/py/phonetic-fr.svg)](https://pypi.python.org/pypi/phonetic-fr/)
[![Pylint](https://github.com/gaspardpetit/phonetic_fr-py/actions/workflows/pylint.yml/badge.svg)](https://github.com/gaspardpetit/phonetic_fr-py/actions/workflows/pylint.yml)[![Python package](https://github.com/gaspardpetit/phonetic_fr-py/actions/workflows/python-package.yml/badge.svg)](https://github.com/gaspardpetit/phonetic_fr-py/actions/workflows/python-package.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/phonetic-fr.svg)](https://pypi.org/project/phonetic-fr/)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


# phonetic-fr
A Soundex-Like Phonetic Algorithm in Python for the French Language

For multilanguage phonetic comparison of words, see [https://github.com/gaspardpetit/phonetic_distance-py](https://github.com/gaspardpetit/phonetic_distance-py)

## Purpose
phonetic-fr implements a Soundex phonetic algorithm, used to compare words by their sound when pronounced in French. The algorithm is particularly useful for tasks such as matching similar-sounding words, especially in cases where the spelling might vary.

## How to install
```{bash}
pip install phonetic-fr
```

## Usage in shell
```{bash}
echo "Le ver vert glisse vers le verre" | phonetic_fr
```
Prints:
```{bash}
L VER VER GLIS VER L VER
```

## Usage in Python
```{py}
from phonetic_fr import phonetic

# Obtain phonetic representation of a word
example = "python"
result = phonetic(example)
print(f"{example} -> {result}")
```

Prints
```
python -> PITON
```

Phonetic results can be used to compare similar sounding words:

```{py}
from phonetic_fr import phonetic

# Compare two names with sounding alike
are_alike = phonetic("Gilles") == phonetic("Jill")
print(f"Gilles sounds like Jill: {are_alike}")
```

Prints
```
Gilles sounds like Jill: True
```

```{py}
from Levenshtein import distance
from phonetic_fr import phonetic

# Improve Levenshtein's distance
word_a = "drapeau"
word_b = "crapaud"
raw_distance = distance(word_a, word_b)
print(f"Levenshtein distance of '{word_a}' and '{word_b}': {raw_distance}")
phonetic_distance = distance(phonetic(word_a), phonetic(word_b))
print(f"Phonetic Levenshtein distance of '{word_a}' and '{word_b}': {phonetic_distance}")
```

Prints
```
Levenshtein distance of 'drapeau' and 'crapaud': 3
Phonetic Levenshtein distance of 'drapeau' and 'crapaud': 1
```

## Description
phonetic-fr is a phonetic algorithm for the French language, similar to the Soundex algorithm used for English. Here is a summary of its functionality:

- **Accent and Case Normalization**: The function starts by normalizing accented characters to their unaccented counterparts and converting lowercase letters to uppercase.

- **Letter Filtering**: It removes any characters that are not alphabetic letters from A to Z.

- **Pre-processing**: The script applies a series of specific pre-processing rules to handle particular letter combinations and sequences, such as converting 'OO' to 'OU', handling silent letters, and adjusting for certain phonetic sounds. These rules are implemented using regular expressions.

- **Special Cases**: The function has hardcoded responses for certain words, such as "TABAC" returning "TABA", ensuring their unique phonetic codes.

- **Main Phonetic Transformation**: The main body of the function uses a series of regular expressions to transform the input string into its phonetic equivalent. This includes handling nasal sounds, silent letters, and specific letter combinations that change their pronunciation in certain contexts.

- **Post-processing**: After the main transformations, the function performs additional post-processing to refine the phonetic code. This includes removing certain terminal letter sequences, further reducing letter repetitions, and other adjustments to align with French phonetics.

- **Terminations**: The function applies final rules to the end of the phonetic code, such as trimming certain letters from the end of the word.

- **Output**: The function returns a phonetic code representing the input string, with a maximum length of 16 characters. If the resulting code is a single letter 'O', it is returned as is. For very short words that may have lost their distinctiveness during processing, the function may revert to earlier saved states of the input string to provide a more accurate phonetic code.

## License

phonetic-fr is released under the MIT license. Feel free to use, modify, and distribute it according to the terms of the license.

## Credits

- [Original PHP implementation](https://github.com/EdouardBERGE/phonetic) by Édouard BERGÉ (December 2007, v1.2).
- Ported to Python by Gaspard Petit.

## Changelog

Changes over the original port are being tracked in the [Changelog](CHANGELOG.md)
