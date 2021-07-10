import numpy as np


def raise_error_if_invalid_state(state: np.ndarray) -> None:
    if state.shape != (4,4):
        raise ValueError(f"State need to be 4x4 matrix. ({state.shape} shape was given)")
    for value in state.flatten():
        if value>255:
            raise ValueError(f"Byte in state can only contain up to 255 ({value} was in the state)")
        if value<0:
            raise ValueError(f"Byte in state can only contain positive integer ({value} was in the state)")
        if value%1!=0:
            raise TypeError(f"Byte in state can only contain positive integer ({value} was in the state)")


class Matrix:
    @property
    def array(self):
        return self._state
    def __init__(self, state: np.ndarray) -> np.ndarray:
        raise_error_if_invalid_state(state)
        self._state = state.astype("uint8")
        return self._state

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(array=\n{np.array2string(self._state, separator=', ')})"

    def __str__(self) -> str:
        array = self._state
        return f"""
| {array[0,0]:02x} {array[0,1]:02x} {array[0,2]:02x} {array[0,3]:02x} |
| {array[1,0]:02x} {array[1,1]:02x} {array[1,2]:02x} {array[1,3]:02x} |
| {array[2,0]:02x} {array[2,1]:02x} {array[2,2]:02x} {array[2,3]:02x} |
| {array[3,0]:02x} {array[3,1]:02x} {array[3,2]:02x} {array[3,3]:02x} |
        """
        
    