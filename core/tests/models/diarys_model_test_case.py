from datetime import datetime, timedelta

from django.test import TestCase
from django.core.exceptions import ValidationError
from model_mommy import mommy

from core.models import Doctors, Diarys, Schedules


class DiarysModelTestCase(TestCase):
    """Class Testing Model Diarys """

    def setUp(self):
        """Initial Test Settings"""

        self.doctor = mommy.make(Doctors, name="Doutor Chapatín")
        self.diary = Diarys()
        self.diary.day = datetime.now().date()
        self.diary.doctor = self.doctor
        self.diary.save()

        for h in range(8, 18):
            schedule = Schedules()
            schedule.hour = h
            schedule.minute = 0
            schedule.diary = self.diary
            schedule.save()

    def tearDown(self):
        """Final method"""

        Doctors.objects.all().delete()
        Diarys.objects.all().delete()
        Schedules.objects.all().delete()

    def test_there_are_fields(self):
        """test the fields the model"""

        fields = ['day', 'doctor']

        for field in fields:
            self.assertTrue(field in dir(
                Diarys), f'Model "Diarys" does not have the field "{field}"')

    def test_there_are_diarys_creation(self):
        """test if you are creating a Diarys correctly"""

        self.assertEquals(Diarys.objects.count(), 1)
        diary = Diarys.objects.all()[0]
        self.assertEquals(diary.day, self.diary.day)
        self.assertEquals(diary.day, datetime.now().date())
        self.assertEquals(diary.doctor.name, self.diary.doctor.name)
        self.assertEquals(diary.doctor.name, "Doutor Chapatín")
        schedules = diary.schedules.all()

        hour = 8
        for schedule in schedules:
            self.assertEquals(schedule.start, f'{hour:02d}:{0:02d}')
            hour += 1

    def test_str_doctors(self):
        """test if str method of Diarys is correctly"""
        self.assertEquals(
            str(self.diary), f'{self.diary.hour:02d}:{self.diary.minute:02d}')

    def test_there_are_not_diarys_creation_when_diarys_exist(self):
        """test if you are creating a Diarys correctly"""

        diary = Diarys()
        diary.day = datetime.now().date()
        diary.doctor = self.doctor
        try:
            diary.save()
            self.assertTrue(False)
        except ValidationError as e:
            ...

    def test_there_are_not_diarys_creation_when_diarys_pass(self):
        """test if you are creating a Diarys correctly"""

        diary = Diarys()
        diary.day = datetime.now().date()+timedelta(days=-5)
        diary.doctor = self.doctor
        try:
            diary.save()
            self.assertTrue(False)
        except ValidationError as e:
            ...
