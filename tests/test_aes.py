import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
import numpy as np
from aesjosephus import utils
from aesjosephus import Mode
from aesjosephus.encryptdecrypt import encrypt, decrypt, InvalidModeError

class TestAESInverseProperty(unittest.TestCase):
    n = 5

    def encryptdecrypt(self, mode: str):
        for _ in range(self.n):
            random_string = utils.random_string(16)
            cipherkey = utils.random_string(16)
            ciphertext = encrypt(random_string, cipherkey, mode=mode).to_string()
            plaintext = decrypt(ciphertext, cipherkey, mode=mode).to_string()
            self.assertEqual(random_string, plaintext)

    def test_original(self):
        self.encryptdecrypt(Mode.ORIGINAL)
        
    def test_josephus(self):
        self.encryptdecrypt(Mode.JOSEPHUS)

    def test_modified_aes(self):
        self.encryptdecrypt(Mode.MODIFIED_TIME)
        self.encryptdecrypt(Mode.MODIFIED_ROUND)


class TestAESExampleCase(unittest.TestCase):
    
    def test_aes_encrypt(self):
        plaintext = utils.state_to_string(np.array([
            [0x32, 0x88, 0x31, 0xe0],
            [0x43, 0x5a, 0x31, 0x37],
            [0xf6, 0x30, 0x98, 0x07],
            [0xa8, 0x8d, 0xa2, 0x34]
        ]))
        cipherkey = utils.state_to_string(np.array([
            [0x2b, 0x28, 0xab, 0x09],
            [0x7e, 0xae, 0xf7, 0xcf],
            [0x15, 0xd2, 0x15, 0x4f],
            [0x16, 0xa6, 0x88, 0x3c]
        ]))
        self.assertTrue(np.array_equal(encrypt(plaintext, cipherkey, mode=Mode.ORIGINAL).array,[
            [0x39, 0x02, 0xdc, 0x19],
            [0x25, 0xdc, 0x11, 0x6a],
            [0x84, 0x09, 0x85, 0x0b],
            [0x1d, 0xfb, 0x97, 0x32]
        ]))

class TestInvalidMode(unittest.TestCase):

    def test_invalid_mode(self):
        plaintext = utils.random_string(16)
        cipherkey = utils.random_string(16)
        with self.assertRaises(InvalidModeError):
            encrypt(plaintext, cipherkey, mode="STRING_TEST")
        with self.assertRaises(InvalidModeError):
            encrypt(plaintext, cipherkey, mode=1)

if __name__ == "__main__":
    unittest.main()