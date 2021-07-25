from .state import State
from .key import Key
from .mode import Mode
from . import key
from . import utils 
import numpy as np

def verify_mode(mode: Mode):
    if not isinstance(mode, Mode):
        raise ValueError('Invalid encryption mode specified.')

def encrypt(plaintext: str, cipherkey: str,mode: Mode) -> State:
    verify_mode(mode)

    state = State(utils.string_to_state(plaintext))
    cipherkey = Key(utils.string_to_state(cipherkey))

    def original(state: State, cipherkey: Key) -> State:
        state = State(np.copy(state.array))
        amount_of_round = 10
        round_keys = key.key_schedule(cipherkey, amount_of_round)

        state.add_round_key(cipherkey)
        for round in range(1,amount_of_round):
            state.sub_bytes()
            state.shift_row()
            state.mix_columns()
            state.add_round_key(round_keys[round])
        state.sub_bytes()
        state.shift_row()
        state.add_round_key(round_keys[amount_of_round])

        return state

    def modified_aes(state: State, cipherkey: Key) -> State:
        state = State(np.copy(state.array))
        amount_of_round = 4
        round_keys = key.key_schedule(cipherkey, amount_of_round)

        state.add_round_key(cipherkey)
        for round in range(1,amount_of_round):
            state.sub_bytes()
            state.shift_row()
            state.add_round_key(round_keys[round])
        state.sub_bytes()
        state.shift_row()
        state.add_round_key(round_keys[amount_of_round])

        return state

    def josephus(state: State, cipherkey: Key):
        state = State(np.copy(state.array))
        amount_of_round = 4
        round_keys = key.key_schedule(cipherkey, amount_of_round)

        state.add_round_key(cipherkey)
        for round in range(1,amount_of_round):
            state.sub_bytes()
            state.shift_row_josephus()
            state.add_round_key(round_keys[round])
        state.sub_bytes()
        state.shift_row()
        state.add_round_key(round_keys[amount_of_round])

        return state

    return {
        Mode.ORIGINAL : original,
        Mode.MODIFIED_ORIGINAL : modified_aes,
        Mode.JOSEPHUS : josephus
    }[mode](state, cipherkey)

def decrypt(ciphertext: str, cipherkey: str,mode: Mode) -> State:
    verify_mode(mode)
    state = State(utils.string_to_state(ciphertext))
    cipherkey = Key(utils.string_to_state(cipherkey))

    def original(state: State, cipherkey: Key) -> State:
        state = State(np.copy(state.array))
        amount_of_round = 10
        round_keys = key.key_schedule(cipherkey, amount_of_round)

        state.inv_add_round_key(round_keys[amount_of_round])
        state.inv_shift_row()
        state.inv_sub_bytes()
        for round in range(amount_of_round-1,0,-1):
            state.inv_add_round_key(round_keys[round])
            state.inv_mix_columns()
            state.inv_shift_row()
            state.inv_sub_bytes()
        state.inv_add_round_key(cipherkey)

        return state

    def modified_aes(state: State, cipherkey: Key) -> State:
        state = State(np.copy(state.array))
        amount_of_round = 4
        round_keys = key.key_schedule(cipherkey, amount_of_round)

        state.inv_add_round_key(round_keys[amount_of_round])
        state.inv_shift_row()
        state.inv_sub_bytes()
        for round in range(amount_of_round-1,0,-1):
            state.inv_add_round_key(round_keys[round])
            state.inv_shift_row()
            state.inv_sub_bytes()
        state.inv_add_round_key(cipherkey)

        return state

    def josephus(state: State, cipherkey: Key):
        state = State(np.copy(state.array))
        amount_of_round = 4
        round_keys = key.key_schedule(cipherkey, amount_of_round)

        state.inv_add_round_key(round_keys[amount_of_round])
        state.inv_shift_row()
        state.inv_sub_bytes()
        for round in range(amount_of_round-1,0,-1):
            state.inv_add_round_key(round_keys[round])
            state.inv_shift_row_josephus()
            state.inv_sub_bytes()
        state.inv_add_round_key(cipherkey)

        return state
    
    return {
        Mode.ORIGINAL : original,
        Mode.MODIFIED_ORIGINAL : modified_aes,
        Mode.JOSEPHUS : josephus
    }[mode](state, cipherkey)