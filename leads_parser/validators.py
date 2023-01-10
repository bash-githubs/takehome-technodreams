import datetime as d

import phonenumbers
import pytz
from django.conf import settings


def is_time_within_range() -> bool:
    indian_time = pytz.timezone("Asia/Kolkata")
    current_hour = d.datetime.now(indian_time).hour
    if int(settings.UPLOAD_START_HOUR) <= current_hour <= int(settings.UPLOAD_END_HOUR):
        return True
    return False


def is_number_in_international_format(phone_number):
    number = phonenumbers.parse(phone_number)
    return True if phonenumbers.is_valid_number(number) else False
