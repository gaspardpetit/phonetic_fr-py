"""Unit tests for phonetic_fr"""
import unittest
import os
import sys
from collections import OrderedDict

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
# pylint: disable=import-error,wrong-import-position
from phonetic_fr import phonetic

class TestPhonetique(unittest.TestCase):
    """Unit tests for phonetic_fr"""
    @staticmethod
    def read_test_cases(filename):
        """Extract test cases from a file"""
        loaded_cases = OrderedDict()
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                line = line.split('#')[0]
                if line.strip():  # Skip blank lines
                    words = line.strip().split()
                    test_word = words[0]
                    expected_result = words[1] if len(words) > 1 else ''
                    loaded_cases[test_word] = expected_result
        return loaded_cases

    def test_phonetique_from_file(self):
        """Unit tests for phonetic_fr"""
        loaded_cases = self.read_test_cases('tests/test_cases.txt')
        expected_fail = self.read_test_cases('tests/test_cases_faling.txt')

        for test_word, expected_result in loaded_cases.items():
            with self.subTest(input_string=test_word):
                actual_result = phonetic(test_word)
                if actual_result != expected_result:
                    if test_word in expected_fail and actual_result == expected_fail[test_word]:
                        print(f"{test_word} -> {actual_result} " +
                              f"[expecting {expected_result}] IGNORED BECAUSE EXPECTED")
                    else:
                        print(f"{test_word} -> {actual_result} " +
                              f"[expecting {expected_result}]")
                        self.assertEqual(actual_result, expected_result)

def print_all_failing_cases():
    """Prints all failing tests without asserting"""
    test_cases = TestPhonetique.read_test_cases('tests/test_cases.txt')
    i = 0
    for input_string, expected_output in test_cases.items():
        result = phonetic(input_string)
        if result != expected_output:
            i = i + 1
            print(f"{i}: {input_string} -> {result} [expecting {expected_output}]")

if __name__ == '__main__':
    unittest.main()
