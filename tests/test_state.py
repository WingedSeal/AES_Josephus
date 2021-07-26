import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
import numpy as np
from aesjosephus import State
from aesjosephus import Key

class TestStateInverseProperty(unittest.TestCase):
    n = 5

    def test_sub_bytes(self):
        for _ in range(self.n):
            random_array = np.random.randint(256, size=[4,4])
            state = State(random_array)
            state.sub_bytes()
            state.inv_sub_bytes()
            self.assertTrue(np.array_equal(random_array, state.array))
    def test_shift_row_josephus(self):
        for _ in range(self.n):
            random_array = np.random.randint(256, size=[4,4])
            state = State(random_array)
            state.shift_row_josephus()
            state.inv_shift_row_josephus()
            self.assertTrue(np.array_equal(random_array, state.array))
    def test_shift_row(self):
        for _ in range(self.n):
            random_array = np.random.randint(256, size=[4,4])
            state = State(random_array)
            state.shift_row()
            state.inv_shift_row()
            self.assertTrue(np.array_equal(random_array, state.array))
    def test_mix_columns(self):
        for _ in range(self.n):
            random_array = np.random.randint(256, size=[4,4])
            state = State(random_array)
            state.mix_columns()
            state.inv_mix_columns()
            self.assertTrue(np.array_equal(random_array, state.array))
    def test_add_round_key(self):
        for _ in range(self.n):
            random_array = np.random.randint(256, size=[4,4])
            state = State(random_array)
            key = Key(np.random.randint(256, size=[4,4]))
            state.add_round_key(key)
            state.inv_add_round_key(key)
            self.assertTrue(np.array_equal(random_array, state.array))

class TestInvalidState(unittest.TestCase):
    def test_invalid_size(self):
        random_array = np.random.randint(256, size=[5,5])
        with self.assertRaises(ValueError):
            State(random_array)

if __name__ == "__main__":
    unittest.main()