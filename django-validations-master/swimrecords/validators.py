from django.core.exceptions import ValidationError
from datetime import datetime, timezone
from django.utils import timezone

import re


def validate_stroke(stroke):
    valid_strokes = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    
    if stroke.lower() not in valid_strokes:
        raise ValidationError(f'{stroke} is not a valid stroke')

def validate_date(record_date):
    if record_date > timezone.now():
        raise ValidationError("Can't set record in the future.")

def validate_new_record(record_broken_date):
    # current_record = SwimRecord.objects.get()
    if record_broken_date < timezone.now():
        raise ValidationError("Can't break record before record was set.")
        