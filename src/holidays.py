import datetime
import re

import requests
from bs4 import BeautifulSoup

HOLIDAY_SITE = "https://smart.net.ua/kalendar-svyat/"

MONTH_NAMES = [
    "січня",
    "лютого",
    "березня",
    "квітня",
    "травня",
    "червня",
    "липня",
    "серпня",
    "вересня",
    "жовтня",
    "листопада",
    "грудня",
]


def get_todays_holidays() -> str:
    return get_holidays_by_date(datetime.date.today())


def get_holidays_by_date(date: datetime.date) -> str:
    page = requests.get(HOLIDAY_SITE)
    bs = BeautifulSoup(page.text, features="html.parser")

    return bs.find_all(string=re.compile(_date_to_repr(date)), limit=1)[0]


def _date_to_repr(date: datetime.date) -> str:
    return f"{date.day} {MONTH_NAMES[date.month]}"
