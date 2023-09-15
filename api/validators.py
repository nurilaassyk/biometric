from django.core.validators import RegexValidator
from rest_framework.exceptions import ValidationError


class IINValidator(RegexValidator):
    regex = r'^[0-9]{12}$'


def iin_validate(value):
    num = 0
    j = 1

    try:
        for i in range(0, len(value) - 1):
            num += int(value[i]) * j
            j += 1

        if num % 11 == 10:
            num = 0
            j = 3
            for i in range(0, len(value) - 1):
                num += int(value[i]) * j
                j += 1
                if j == 12:
                    j = 1
    except Exception as e:
        raise InvalidIin

    if len(value) != 12:
        raise InvalidIin

    if num % 11 != int(value[11]):
        raise InvalidIin

    if not value.isdigit():
        raise InvalidIin


class InvalidIin(ValidationError):
    default_detail = 'Invalid IIN'
