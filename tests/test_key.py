import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
import numpy as np
from aesjosephus import Key, key_schedule

class TestExampleKeySchedule(unittest.TestCase):
    def test_key_schedule(self):
        cipherkey = Key(np.array([
            [0x2b, 0x28, 0xab, 0x09],
            [0x7e, 0xae, 0xf7, 0xcf],
            [0x15, 0xd2, 0x15, 0x4f],
            [0x16, 0xa6, 0x88, 0x3c]
        ]))
        keys = key_schedule(cipherkey, 10)
        self.assertTrue(np.array_equal(keys[1].array,np.array([
            [0xa0, 0x88, 0x23, 0x2a],
            [0xfa, 0x54, 0xa3, 0x6c],
            [0xfe, 0x2c, 0x39, 0x76],
            [0x17, 0xb1, 0x39, 0x05]
        ])
        ))
        self.assertTrue(np.array_equal(keys[10].array,np.array([
            [0xd0, 0xc9, 0xe1, 0xb6],
            [0x14, 0xee, 0x3f, 0x63],
            [0xf9, 0x25, 0x0c, 0x0c],
            [0xa8, 0x89, 0xc8, 0xa6]
        ])
        ))

if __name__ == "__main__":
    unittest.main()