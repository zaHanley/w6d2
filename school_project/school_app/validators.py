import re #regex library
from django.core.exceptions import ValidationError #built in exceptions that come w django

def validate_locker_combination(combination):
    pattern = r"(\d{1,2})-(\d{1,2})-(\d{1,2})"
    match = re.search(pattern, combination) #return bool

    if not match:
        raise ValidationError("Invalid combination")