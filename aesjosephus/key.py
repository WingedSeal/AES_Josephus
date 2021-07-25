from .matrix import Matrix
from . import constant

import numpy as np
from typing import List


class Key(Matrix):
    def __init__(self, array: np.ndarray) -> None:
        self._state = super().__init__(array)

def a_key_schedule(round_key: Key, round: int) -> Key:
    """ Generate new Roundkey from old one"""
    new_round_key = np.empty([4, 4], dtype="uint8")
    for row in range(4):
        new_round_key[row,0] = constant.S_BOX[round_key.array[row-3,3]] ^ round_key.array[row,0] ^ constant.R_CON[row,round-1]
        for column in range(1,4):
            new_round_key[row,column] = round_key.array[row,column] ^ new_round_key[row,column-1]
    return Key(new_round_key)

def key_schedule(cipherkey: Key, amount_of_round: int) -> List[Key]:
    """ Generate a list of Roundkey """
    keys = {
        "cipherkey" : cipherkey,
        1 : a_key_schedule(cipherkey, 1)
    }
    for round in range(2,amount_of_round+1):
        keys[round] = a_key_schedule(keys[round-1], round)
    return keys

    