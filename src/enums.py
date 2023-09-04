from enum import Enum

# actions
class Action(Enum):
    RESERVE = 1
    CANCEL_RESERVATION = 2
    PRINT_SEAT_MAP = 3
    SAVE = 4
    IMPORT = 5
    QUIT_PROGRAM = 6

# seat statuses
class SeatStatus(Enum):
    INVALID = 0
    VALID = 1
    RESERVED = 2
