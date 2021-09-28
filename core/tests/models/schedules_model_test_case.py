from datetime import datetime
from django.test import TestCase
from model_mommy import mommy

from core.models import Schedules, Diarys


class SchedulesModelTestCase(TestCase):
    """Class Testing Model Schedules """

    def setUp(self):
        """Initial Test Settings"""
        self.hour = datetime.now().time()
        self.diary =  mommy.make(Diarys)
        self.schedules = mommy.make(Schedules, hour=self.hour, diary=self.diary)

    def tearDown(self):
        """Final method"""
        Schedules.objects.all().delete()
        Diarys.objects.all().delete()

    def test_there_are_fields(self):
        """test the fields the model"""

        fields = ['hour', 'diary']

        for field in fields:
            self.assertTrue(field in dir(
                Schedules), f'Model "Schedules" does not have the field "{field}"')

    def test_there_are_schedules_creation(self):
        """test if you are creating a Schedules correctly"""

        self.assertEquals(Schedules.objects.count(), 1)
        schedules = Schedules.objects.all()[0]
        self.assertEquals(schedules.hour, self.schedules.hour)
        self.assertEquals(schedules.diary, self.schedules.diary)

    def test_str_schedules(self):
        """test if str method of Schedules is correctly"""
        
        hour = str(self.schedules.hour).split(':')
        self.assertEquals(str(self.schedules),
                         f'{hour[0]}:{hour[1]}')
