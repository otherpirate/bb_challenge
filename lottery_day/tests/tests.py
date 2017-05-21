from unittest import TestCase
from datetime import datetime, timedelta
from src.main import WEDNESDAY, SATURDAY, LOTTERY_DAYS, LOTTERY_HOUR, \
    get_next_lottery_date


class NexLotteryDayTests(TestCase):

    def test_lottery_days(self):
        self.assertEqual(len(LOTTERY_DAYS), 2)
        self.assertIn(WEDNESDAY, LOTTERY_DAYS)
        self.assertIn(SATURDAY, LOTTERY_DAYS)

    def test_lottery_week_day(self):
        self.assertEqual(WEDNESDAY, 2)
        self.assertEqual(SATURDAY, 5)

    def test_lottery_hour(self):
        self.assertEqual(LOTTERY_HOUR, 20)

    def test_without_date(self):
        expected_date = datetime.now()
        if expected_date.hour > LOTTERY_HOUR:
            expected_date = expected_date + timedelta(days=1)
        expected_date = expected_date.replace(
            hour=LOTTERY_HOUR, minute=0, second=0, microsecond=0
        )
        while not expected_date.weekday() in LOTTERY_DAYS:
            expected_date = expected_date + timedelta(days=1)
        next_lottery = get_next_lottery_date()
        self.assertEqual(next_lottery, expected_date)

    def test_date_after_hour(self):
        expected_date = datetime(day=27, month=5, year=2017, hour=LOTTERY_HOUR)

        after_hour_date = datetime(
            day=24, month=5, year=2017, hour=LOTTERY_HOUR + 1
        )
        next_lottery = get_next_lottery_date(after_hour_date)
        self.assertEqual(next_lottery, expected_date)

    def test_date_before_hour(self):
        expected_date = datetime(day=24, month=5, year=2017, hour=LOTTERY_HOUR)

        after_hour_date = datetime(
            day=24, month=5, year=2017, hour=LOTTERY_HOUR - 1
        )
        next_lottery = get_next_lottery_date(after_hour_date)
        self.assertEqual(next_lottery, expected_date)

    def test_next_day(self):
        expected_date = datetime(day=31, month=5, year=2017, hour=LOTTERY_HOUR)

        after_hour_date = datetime(
            day=28, month=5, year=2017, hour=LOTTERY_HOUR + 1
        )
        next_lottery = get_next_lottery_date(after_hour_date)
        self.assertEqual(next_lottery, expected_date)
