# Phonetic-FR
A Soundex-Like Phonetic Algorithm in Python for the French Language

## Purpose
Phonetic-FR implements a Soundex phonetic algorithm, used to compare words by their sound when pronounced in French. The algorithm is particularly useful for tasks such as matching similar-sounding words, especially in cases where the spelling might vary.

## How to install
```{bash}
pip install phonetic_fr
```

## Usage in shell
```{bash}
echo "Le ver vert glisse vers le verre" | phonetic-fr
```
Prints:
```{bash}
LE VE VER GLIS VER LE VER
```

## Usage in Python
```{py}
from phonetic_fr import phonetic

french_word = "Python"
soundex_code = phonetic(french_word)
print(f"The Phonetic code for '{input_word}' is: {soundex_code}")
```

Prints
```
The Phonetic code for 'Python' is: PITON
```

Phonetic results can be used to compare similar sounding words:

```{py}
from phonetic_fr import phonetic
print(phonetic("Gilles") == phonetic("Jill"))
```

Prints
```
True
```

## Description
Phonetic-FR is a phonetic algorithm for the French language, similar to the Soundex algorithm used for English. Here is a summary of its functionality:

- **Accent and Case Normalization**: The function starts by normalizing accented characters to their unaccented counterparts and converting lowercase letters to uppercase.

- **Letter Filtering**: It removes any characters that are not alphabetic letters from A to Z.

- **Pre-processing**: The script applies a series of specific pre-processing rules to handle particular letter combinations and sequences, such as converting 'OO' to 'OU', handling silent letters, and adjusting for certain phonetic sounds. These rules are implemented using regular expressions.

- **Special Cases**: The function has hardcoded responses for certain words, such as "TABAC" returning "TABA", ensuring their unique phonetic codes.

- **Main Phonetic Transformation**: The main body of the function uses a series of regular expressions to transform the input string into its phonetic equivalent. This includes handling nasal sounds, silent letters, and specific letter combinations that change their pronunciation in certain contexts.

- **Post-processing**: After the main transformations, the function performs additional post-processing to refine the phonetic code. This includes removing certain terminal letter sequences, further reducing letter repetitions, and other adjustments to align with French phonetics.

- **Terminations**: The function applies final rules to the end of the phonetic code, such as trimming certain letters from the end of the word.

- **Output**: The function returns a phonetic code representing the input string, with a maximum length of 16 characters. If the resulting code is a single letter 'O', it is returned as is. For very short words that may have lost their distinctiveness during processing, the function may revert to earlier saved states of the input string to provide a more accurate phonetic code.

## License

Phonetic-FR is released under the MIT license. Feel free to use, modify, and distribute it according to the terms of the license.

## Credits

- [Original PHP implementation](https://github.com/EdouardBERGE/phonetic) by Édouard BERGÉ (December 2007, v1.2).
- Ported to Python by Gaspard Petit.
