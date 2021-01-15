from babel.dates import format_date
from ckantoolkit import h
from datetime import datetime


def localized_date(date_string):
    d = datetime.strptime(date_string, '%Y%m%d')

    return format_date(d, locale=h.lang())
