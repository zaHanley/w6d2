from django.test import TestCase
from .models import Locker
from django.core.exceptions import ValidationError


class school_tests(TestCase):
    def test_01_create_locker_wrong_combo(self):

        new_locker = Locker(locker_number=150, combination='213-435')
        try:
            new_locker.full_clean() # runs your validators
        except ValidationError as e:
            self.assertTrue("Invalid combination" in e.message_dict['combination'])

