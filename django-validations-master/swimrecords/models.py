from django.db import models
from django.core import validators as v
from .validators import validate_stroke, validate_date, validate_new_record
from datetime import timedelta, date, datetime
from django.utils import timezone
from django.db.models import F


class SwimRecord(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=100, validators=[validate_stroke])
    distance = models.IntegerField(validators=[v.MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[validate_date])
    record_broken_date = models.DateTimeField(validators=[validate_new_record])





