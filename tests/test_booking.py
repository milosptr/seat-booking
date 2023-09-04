import unittest
from src.core import seatManager
from src.enums import SeatStatus, Action
from src.state import reservedSeats
from src.helpers import getDatetime, formatDatetime, formatSeat, seatValidation

class TestBooking(unittest.TestCase):
  # clear the reservedSeats list before each test
  def setUp(self):
    reservedSeats.clear()

  # getDatetime should return current datetime string with length 26
  def test_getDatetime(self):
    self.assertEqual(len(getDatetime()), 26)

  # format datetime should format any value given, it should not validate the datetime
  def test_formatDatetime(self):
    self.assertEqual(formatDatetime('2021-10-01 12:00:00.000000'), '01/10/2021 12:00:00')
    self.assertEqual(formatDatetime('2021-10-01'), '2021-10-01')

  # basically format seat number should format any value given
  # it should not validate the seat number
  def test_formatSeat(self):
    self.assertEqual(formatSeat(''), '')
    self.assertEqual(formatSeat('A'), 'A')
    self.assertEqual(formatSeat('0'), '0')
    self.assertEqual(formatSeat('A1'), 'A01')
    self.assertEqual(formatSeat('A10'), 'A10')
    self.assertEqual(formatSeat('A100'), 'A100')
    self.assertEqual(formatSeat('A100000000'), 'A100000000')

  def test_seatValidation(self):
    # invalid seat numbers
    self.assertEqual(seatValidation(''), SeatStatus.INVALID.value)
    self.assertEqual(seatValidation('A'), SeatStatus.INVALID.value)
    self.assertEqual(seatValidation('0'), SeatStatus.INVALID.value)
    self.assertEqual(seatValidation('A1'), SeatStatus.INVALID.value)
    self.assertEqual(seatValidation('A100'), SeatStatus.INVALID.value)
    # valid seat numbers
    self.assertEqual(seatValidation('A10'), SeatStatus.VALID.value)
    self.assertEqual(seatValidation('C32'), SeatStatus.VALID.value)
    # reserved seat numbers
    reservedSeats.append('A01')
    self.assertEqual(seatValidation('A01'), SeatStatus.RESERVED.value)

  # testing reserve of non-existing reservation
  def test_manageSeat_RESERVE_A1(self):
    result = seatManager(Action.RESERVE.value, 'A01')
    self.assertTrue(result)

  # testing reserve of existing reservation
  def test_manageSeat_RESERVE_A1_twice(self):
    reservedSeats.append('A01')
    result = seatManager(Action.RESERVE.value, 'A01')
    self.assertFalse(result)

  # testing invalid seat number (too short)
  def test_manageSeat_RESERVE_A1_invalid(self):
    result = seatManager(Action.RESERVE.value, 'A1')
    self.assertFalse(result)

  # testing invalid seat number (too long)
  def test_manageSeat_RESERVE_A1_invalid2(self):
    result = seatManager(Action.RESERVE.value, 'A100')
    self.assertFalse(result)

  # testing cancel of existing reservation
  def test_manageSeat_CANCEL_A1(self):
    reservedSeats.append('A01')
    result = seatManager(Action.CANCEL_RESERVATION.value, 'A01')
    self.assertTrue(result)

  # testing cancel of non-existing reservation
  def test_manageSeat_CANCEL_undefined_seat(self):
    result = seatManager(Action.CANCEL_RESERVATION.value, 'A01')
    self.assertFalse(result)
