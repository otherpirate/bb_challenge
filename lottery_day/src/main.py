from datetime import datetime, timedelta

WEDNESDAY = 2
SATURDAY = 5
LOTTERY_DAYS = [WEDNESDAY, SATURDAY]
LOTTERY_HOUR = 20


def get_next_lottery_date(current_date=None):
    if not current_date:
        current_date = datetime.now()

    if current_date.hour > LOTTERY_HOUR:
        current_date = current_date + timedelta(days=1)
    current_date = current_date.replace(
        hour=LOTTERY_HOUR, minute=0, second=0, microsecond=0
    )

    while not current_date.weekday() in LOTTERY_DAYS:
        current_date = current_date + timedelta(days=1)

    return current_date
