import numpy as np
import random
from textwrap import wrap
from string import ascii_letters, digits, punctuation

def string_to_state(string: str) -> np.ndarray:
    if len(string) != 16: 
        raise ValueError(f"Length of given string must be 16. ({len(string)} was given.)")
    return np.array([ord(char) for char in string],dtype="int16").reshape(4,4)

def state_to_string(state: np.ndarray) -> str:
    if state.shape != (4,4):
        raise ValueError(f"State need to be 4x4 matrix. ({state.shape} shape was given)")
    return ''.join([chr(byte) for byte in state.flatten()])

def string_to_hex(string: str) -> str:
    return ''.join(f'{ord(char):02x}' for char in string)

def hex_to_string(string: str) -> str:
    if len(string)%2==1:
        raise ValueError(f"string's length is an odd number ({len(string)})")
    return ''.join([chr(int(byte, 16)) for byte in wrap(string, 2)])

def random_string(length: int, excluded: str = None) -> str:
    valid_char = list(ascii_letters + digits + punctuation)
    if excluded is not None:
        valid_char.remove(excluded)
    return ''.join(random.choice(valid_char) for _ in range(length))