import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
import random
import numpy as np
from aesjosephus import utils

class TestRandomString(unittest.TestCase):
    def test_string_length_match(self):
        length = random.randrange(32)
        string = utils.random_string(length)
        self.assertEqual(length, len(string))
    def test_excluding(self):
        length = random.randrange(32)
        char = utils.random_string(1)
        string = utils.random_string(length, char)
        self.assertFalse(char in string)

class TestUtilsError(unittest.TestCase):
    def test_string_to_state(self):
        length = random.choice([number for number in range(0,32) if number != 16])
        string = utils.random_string(length)
        with self.assertRaises(ValueError):
            utils.string_to_state(string)
        with self.assertRaises(TypeError):
            utils.string_to_state(length)

    def test_state_to_string(self):
        random_array = np.random.randint(256, size=[5,5])
        with self.assertRaises(ValueError):
            utils.state_to_string(random_array)
    def test_hex_to_string(self):
        with self.assertRaises(ValueError):
            utils.hex_to_string("12345")
            utils.hex_to_string("%%%%")

if __name__ == "__main__":
    unittest.main()