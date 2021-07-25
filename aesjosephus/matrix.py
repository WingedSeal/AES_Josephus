import numpy as np
     
            
class Matrix:
    @property
    def array(self):
        return self._state
    def __init__(self, state: np.ndarray) -> np.ndarray:
        if state.shape != (4,4):
            raise ValueError(f"State need to be 4x4 matrix. ({state.shape} shape was given)")
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
        
    