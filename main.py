from src.enums import Action
from src.core import printSeatMap, seatManager, saveToFile, importFromFile
from src.helpers import formatSeat
from src.state import reservedSeats

def printActions() -> None:
    # Print the menu options and ask the user to choose one of them
    print("-" * 30)
    print("👉 Please choose one of the following options:")
    for action in Action:
        print(f'{action.value}. {action.name.replace("_", " ").title()}')

def manageSeatAction(action: Action, seat: str) -> bool:
    # If the input is Q, exit the function
    if seat == 'Q':
      return False
    status = seatManager(action, seat)

    # If the action is reserve, add the seat to the reservedSeats list
    if status and action == Action.RESERVE.value:
      reservedSeats.append(seat)

    # If the action is cancel reservation, remove the seat from the reservedSeats list
    if status and action == Action.CANCEL_RESERVATION.value:
      reservedSeats.remove(seat)
    return status

if __name__ == '__main__':
  while True:
    # Print the menu options and ask the user to choose one of them
    printActions()

    # Ask the user to choose an option
    # If the input is not a number, print the error message and ask the user to choose again
    try:
      action: int = int(input("Option: "))
    except:
      print("-" * 30)
      print('⛔️ Invalid option. Please select option again.')
      continue

    # Print the line separator for better readability
    print("-" * 30)

    # If user wants to reserve or cancel a reservation, ask for the seat number
    if action == Action.RESERVE.value or action == Action.CANCEL_RESERVATION.value:
        ENTER_TEXT: str = 'reserve' if action == Action.RESERVE.value else 'cancel'
        try:
          seat = formatSeat(input(f'Please enter the seat number you want to {ENTER_TEXT} or q/Q to go back: ').upper())
        except Exception as e:
          print('⛔️ Invalid input. Please try again.')
          continue
        manageSeatAction(action, seat)

    # If user wants to print the seat map, print the seat map
    elif action == Action.PRINT_SEAT_MAP.value:
        printSeatMap()

    # If user wants to save the reservations to a file, save the reservations to a file
    elif action == Action.SAVE.value:
        saveToFile()

    # If user wants to import the reservations from a file, clear the current reservations and import the reservations from a file
    elif action == Action.IMPORT.value:
        reservedSeats.clear()
        reservedSeats.extend(importFromFile())

    # If user wants to quit the program, print the goodbye message and exit the program
    elif action == Action.QUIT_PROGRAM.value:
        print('👋 Bye!')
        break

    # If the input is not a valid option, print the error message and ask the user to choose again
    else:
      print('⛔️ Invalid option. Please select option again.')

    # Ask the user to press ENTER to open the menu again or q/Q to exit
    # If the input is Q, print the goodbye message and exit the program
    print('Press ENTER to open the menu again or q/Q to exit.')
    if input().upper() == 'Q':
        print('👋 Bye!')
        break
