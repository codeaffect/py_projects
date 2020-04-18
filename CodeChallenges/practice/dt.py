from datetime import date
from datetime import time
from datetime import datetime
from datetime import timezone
from datetime import timedelta


def printDate_Today():
    print(date.today())


def printDate_Now():
    print(datetime.now())


def datetimes():
    # printDate_Today()
    printDate_Now()
    print('Max Date: ', date.max)
    print('Min Date: ', date.min)
    print(date(2020, 9, 23))
    print(time(10, 11, 12))
    dt = datetime.now()
    print(str(dt))


def tdeltas():
    print(timedelta(days=365))
    print(timedelta(weeks=40))
    print(timedelta(weeks=40, days=20, hours=10))


def dates():
    print(date.today())
    print(date.fromtimestamp(1000))
    print(date.fromordinal(date.max.toordinal()-1))
    print(date.fromisoformat('2020-01-23'))
    print(date(2020, 1, 23).isocalendar())
    print(date.today().toordinal())


dates()
