import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

import unittest
from unittest import TestCase
from phonetic import phonetic

class TestPhonetique(unittest.TestCase):
    @staticmethod
    def read_test_cases(filename):
        test_cases = []
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():  # Skip blank lines
                    words = line.strip().split()
                    input_string = words[0]
                    expected_output = words[1] if len(words) > 1 else ''
                    test_cases.append((input_string, expected_output))
        return test_cases

    def test_phonetique_from_file(self):
        print(os.getcwd())
        test_cases = self.read_test_cases('tests/test_cases.txt')

        for input_string, expected_output in test_cases:
            with self.subTest(input_string=input_string):
                result = phonetic(input_string)
                if result != expected_output:
                    print(f"{input_string} -> {result} [expecting {expected_output}]")
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()


class Test(TestCase):
    def test_phonetique(self):
        self.fail()
