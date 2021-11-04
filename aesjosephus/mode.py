from enum import Enum, auto

class Mode(Enum):
    ORIGINAL = auto()
    JOSEPHUS = auto()
    MODIFIED_ROUND = auto()
    MODIFIED_TIME = auto()