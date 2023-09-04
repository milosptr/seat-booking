from src.enums import SeatStatus, Action
from src.helpers import formatSeat, formatDatetime, getDatetime, seatValidation
from src.state import COLUMNS, ROWS, RESERVATIONS_FILENAME, reservedSeats
import json

def printSeatMap() -> None:
    # Print the seat map
    print("   ", end=" ")
    for column in COLUMNS:
        print(column, end="  ")
    print()

    # Loop through the rows and columns and print the seat map
    for row in ROWS:
        # Format row numbers
        print(f'{row:02d}', end="  ")

        for column in COLUMNS:

            # Format the seat number
            seat = formatSeat(f'{column}{row}')

            # If the seat is reserved, print 'R'
            if seat in reservedSeats:
                print('R', end='  ')

            # If the seat is not reserved, print '.'
            else:
                print('.', end='  ')
        print()

def seatManager(action: Action, seat: str) -> bool:
    # text to print based on the action type
    SUCCESS_TEXT: str = 'reserved' if action == Action.RESERVE.value else 'cancelled'

    # Validate the seat number
    seatStatus = seatValidation(seat)

    if seatStatus == SeatStatus.INVALID.value:
        print("⛔️ Invalid seat number.")
        return False
    if action == Action.RESERVE.value and seatStatus == SeatStatus.RESERVED.value:
        print("⛔️ This seat has been reserved.")
        return False
    if action == Action.CANCEL_RESERVATION.value and seat not in reservedSeats:
        print("⛔️ This seat has not been reserved.")
        return False

    print(f'✅ You have {SUCCESS_TEXT} seat {seat}.')
    return True

def saveToFile() -> None:
    # If there are no reservations, print the error message and exit the function
    if len(reservedSeats) == 0:
        print('⛔️ No reservations to save.')
        return

    # Prepare the data to be saved to file
    data = {
        'timestamp': str(getDatetime()),
        'reservations': reservedSeats
    }

    # Save the data to file
    with open(RESERVATIONS_FILENAME, 'w') as reservationsFile:
        json.dump(data, reservationsFile)
    print('✅ Reservations saved to file.')

def importFromFile() -> list[str]:
    try:
        with open(RESERVATIONS_FILENAME, 'r') as reservationsFile:
            data = json.load(reservationsFile)
            datetime = data['timestamp']
            print(f'✅ Reservations from a date {formatDatetime(datetime)} successfuly imported.')
            return data['reservations']
    except Exception as e:
        print(f'⛔️ Error reading reservations from file. e: {str(e)}')
        return []
