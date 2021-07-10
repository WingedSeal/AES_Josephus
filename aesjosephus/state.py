from .matrix import Matrix
from .key import Key
from . import utils
from . import constant

import numpy as np
from math import floor, sqrt


def josephus_order(n: int,k: int) -> np.ndarray:
    item_array = list(range(n))
    victim_index = 0
    order = []
    while len(item_array) > 0:
        victim_index = (victim_index+k-1) % len(item_array)
        victim_id = item_array.pop(victim_index)
        if victim_id<16:
            order.append(victim_id)
    return np.array(order, dtype="uint8")

def shift_row_josephus_order(state: np.ndarray) -> np.ndarray:
    n_josephus = floor(sqrt(np.sum(state)))
    k_josephus = floor(sqrt(np.bitwise_xor.reduce(state.flatten())))
    if n_josephus < 16: 
        n_josephus = 16
    return josephus_order(n_josephus,k_josephus)

def substitute(state, lookup_table: np.ndarray) -> None:
    for row in range(4):
        for column in range(4):
            state[row,column] = lookup_table[state[row,column]]

def mul(byte: int, n: int) -> int:
    if n==1:
        return byte
    return constant.MODULAR_MULTIPLICATION_TABLE[n][byte]


class State(Matrix):
    def __init__(self, array: np.ndarray) -> None:
        self._state = super().__init__(array)
    
#---------- 4 main steps ----------#

    def sub_bytes(self) -> None:
        substitute(self._state, constant.S_BOX)
    def inv_sub_bytes(self) -> None:
        substitute(self._state, constant.INV_S_BOX)

    def shift_row_josephus(self) -> None:  
        order = shift_row_josephus_order(self._state)
        self._state = np.array([self._state.flatten()[np.where(order==i)] for i in range(16)], dtype="uint8").reshape(4,4)
    def inv_shift_row_josephus(self) -> None:
        order = shift_row_josephus_order(self._state)
        self._state = np.array([self._state.flatten()[order[i]] for i in range(16)], dtype="uint8").reshape(4,4)

    def shift_row(self) -> None:
        self._state = np.array([
        [self._state[0,0], self._state[0,1], self._state[0,2], self._state[0,3]],
        [self._state[1,1], self._state[1,2], self._state[1,3], self._state[1,0]],
        [self._state[2,2], self._state[2,3], self._state[2,0], self._state[2,1]],
        [self._state[3,3], self._state[3,0], self._state[3,1], self._state[3,2]]
    ], dtype="uint8")
    def inv_shift_row(self) -> None:
        self._state = np.array([
        [self._state[0,0], self._state[0,1], self._state[0,2], self._state[0,3]],
        [self._state[1,3], self._state[1,0], self._state[1,1], self._state[1,2]],
        [self._state[2,2], self._state[2,3], self._state[2,0], self._state[2,1]],
        [self._state[3,1], self._state[3,2], self._state[3,3], self._state[3,0]]
    ], dtype="uint8")

    def mix_columns(self) -> None:
        state = np.empty([4,4], dtype="uint8")
        table = np.array([
            [2,3,1,1],
            [1,2,3,1],
            [1,1,2,3],
            [3,1,1,2]
        ], dtype="uint8")
        for column in range(4):
            for row in range(4):
                state[row, column] = mul(self._state[0,column], table[row,0]) ^ mul(self._state[1,column], table[row,1]) ^ mul(self._state[2,column], table[row,2]) ^ mul(self._state[3,column], table[row,3])
        self._state = state
    def inv_mix_columns(self) -> None:
        state = np.empty([4,4], dtype="uint8")
        table = np.array([
            [14,11,13,9],
            [9,14,11,13],
            [13,9,14,11],
            [11,13,9,14]
        ], dtype="uint8")
        for column in range(4):
            for row in range(4):
                state[row, column] = mul(self._state[0,column], table[row,0]) ^ mul(self._state[1,column], table[row,1]) ^ mul(self._state[2,column], table[row,2]) ^ mul(self._state[3,column], table[row,3])
        self._state = state

    def add_round_key(self,round_key: Key) -> None:
        self._state = self._state ^ round_key.array
    def inv_add_round_key(self, *args, **kwargs):
        self.add_round_key(*args, **kwargs)

    def to_string(self) -> str:
        return utils.state_to_string(self._state)

    