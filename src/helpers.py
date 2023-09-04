from datetime import datetime
from src.enums import SeatStatus
from src.state import COLUMNS, ROWS, reservedSeats

def formatDatetime(timestamp: str) -> str:
    # If the timestamp is valid, return the timestamp in the format 'D/M/Y H:M:S'
    try:
      dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
      return dt.strftime('%d/%m/%Y %H:%M:%S')
    # If the timestamp is invalid, return the timestamp as is
    except ValueError:
      return timestamp

# Gets the current date and time in the format 'Y-M-D H:M:S.f'
def getDatetime() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

# Formats the seat number to the format 'A01' or 'A10'
# If the seat number is invalid, return the seat number as is
def formatSeat(seat: str) -> str:
    if len(seat) < 2:
        return seat
    return f'{seat[0]}{int(seat[1:]):02d}'

# Validates the seat number
def seatValidation(seat: str) -> int:

    # If the seat number is invalid, return SeatStatus.INVALID
    if len(seat) <= 2:
        return SeatStatus.INVALID.value

    # If the seat number is valid, return SeatStatus.VALID
    if seat[0] not in COLUMNS or int(seat[1:]) not in ROWS:
        return SeatStatus.INVALID.value

    # If the seat number is reserved, return SeatStatus.RESERVED
    if seat in reservedSeats:
        return SeatStatus.RESERVED.value

    # In all other cases the seat number is SeatStatus.VALID
    return SeatStatus.VALID.value
