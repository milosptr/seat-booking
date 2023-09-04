# Python Seat Reservation System

This project provides a simple console-based interface to manage seat reservations. It allows users to reserve seats, cancel reservations, print the current seating map, save reservations to a file, and import reservations from a file.

## Folder Structure

```
.
├── src/
│   ├── core.py         # Core functionalities for seat reservation system
│   ├── helpers.py      # Utility functions to assist core functionalities
│   ├── state.py        # Maintains the current state of reserved seats
│   └── enums.py        # Enumerations used in the system
├── tests/
│   └── test_booking.py # Unit tests for the booking system
├── main.py             # Main entry point for the application
└── reservations.json   # (Generated if saved) Contains saved seat reservations
```

## Getting Started

1. Ensure you have Python installed on your system.
2. Clone the repository.
3. Navigate to the project root directory in your terminal.
4. Run `main.py` to start the application:
   ```
   python main.py
   ```

## Features

- **Reserve Seats**: Allows users to reserve available seats.
- **Cancel Reservations**: Users can cancel their existing reservations.
- **Print Seating Map**: Displays a visual representation of the seating with reserved seats marked.
- **Save to File**: Saves the current reservations to `reservations.json` in the project root.
- **Import from File**: Imports reservations from `reservations.json`, overwriting the current reservations.

## Unit Tests

Unit tests are provided in the `tests/` directory. Specifically, refer to `tests/test_booking.py`.

To run the tests:
```
python -m unittest tests/test_booking.py
```

## Contribute

Feel free to fork this repository, make your improvements and then create a pull request.
