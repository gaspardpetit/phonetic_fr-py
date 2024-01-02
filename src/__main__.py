import sys
import argparse
from .phonetic_fr import phonetic, __version__

def phonetic_with_whitespace(input_str):
    current_word = ""
    result = ""
    for char in input_str:
        if char.isspace():
            if current_word:
                result += phonetic(current_word) + char
                current_word = ""
            else:
                result += char
        else:
            current_word += char
    if current_word:
        result += phonetic(current_word)
    return result

def main():
    parser = argparse.ArgumentParser(description='French Soundex Phonetics Tool - Convert French words to phonetic representation while preserving whitespace.',
                                     epilog='Input words can be provided through stdin. Example: echo "word1  word2" | python -m phonetic_fr.phonetic_fr')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}', help='Show the version number')
    args = parser.parse_args()

    lines = sys.stdin.readlines()

    if not lines:
        print("Error: No input provided through stdin.")
        parser.print_help()
        sys.exit(1)

    for line in lines:
        result_line = phonetic_with_whitespace(line)
        print(result_line.strip())


if __name__ == '__main__':
    main()
