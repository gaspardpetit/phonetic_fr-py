"""Command line tool to convert French words to a phonetic represnetation"""
import sys
import argparse
from .__init__ import phonetic_text, __version__

def main():
    """Entrypoint"""
    parser = argparse.ArgumentParser(
        description='French Soundex Phonetics Tool - Convert French words ' +
        'to phonetic representation while preserving whitespace.',
        epilog='Input words can be provided through stdin. '+
        'Example: echo "word1  word2" | python -m phonetic_fr.phonetic_fr')
    parser.add_argument(
        '-v', '--version', action='version', version=f'%(prog)s {__version__}', 
        help='Show the version number')

    lines = sys.stdin.readlines()

    if not lines:
        print("Error: No input provided through stdin.")
        parser.print_help()
        sys.exit(1)

    for line in lines:
        result_line = phonetic_text(line)
        print(result_line.strip())


if __name__ == '__main__':
    main()
