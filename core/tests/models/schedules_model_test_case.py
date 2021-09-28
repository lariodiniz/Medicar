from django.test import TestCase
from model_mommy import mommy
from core.models import Schedules


class SchedulesModelTestCase(TestCase):
    """Class Testing Model Schedules """

    def setUp(self):
        """Initial Test Settings"""
        self.schedules = mommy.make(Schedules, hour=11, minute=0)

    def tearDown(self):
        """Final method"""
        Schedules.objects.all().delete()

    def test_there_are_fields(self):
        """test the fields the model"""

        fields = ['hour', 'minute', 'diary']

        for field in fields:
            self.assertTrue(field in dir(
                Schedules), f'Model "Schedules" does not have the field "{field}"')

    def test_there_are_schedules_creation(self):
        """test if you are creating a Schedules correctly"""

        self.assertEquals(Schedules.objects.count(), 1)
        schedules = Schedules.objects.all()[0]
        self.assertEquals(schedules.hour, self.schedules.hour)
        self.assertEquals(schedules.minute, self.schedules.minute)
        self.assertEquals(schedules.diary, self.schedules.diary)

    def test_str_schedules(self):
        """test if str method of Schedules is correctly"""
        self.assertEquals(str(self.schedules),
                          f'{self.schedules.start} - {self.schedules.finish}')

    def test_start_schedules(self):
        """test if start method of Schedules is correctly"""
        self.assertEquals(
            f'{self.schedules.hour:02d}:{self.schedules.minute:02d}', f'{self.schedules.start}')

    def test_finish_schedules(self):
        """test if finish method of Schedules is correctly"""
        hour_finish = self.schedules.hour + 1
        if hour_finish > 23:
            hour_finish = 0
        finish = f'{hour_finish:02d}:{self.schedules.minute:02d}'

        self.assertEquals(finish, f'{self.schedules.finish}')

    def test_finish_schedules_hour_23(self):
        """test if finish method of Schedules is correctly when hour is 23"""
        schedules = mommy.make(Schedules, hour=23, minute=55)
        finish = f'{0:02d}:{55:02d}'

        self.assertEquals(finish, f'{schedules.finish}')
