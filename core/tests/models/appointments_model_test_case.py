from datetime import datetime, timedelta

from django.test import TestCase
from django.core.exceptions import ValidationError
from model_mommy import mommy
from django.contrib.auth.models import User

from core.models import Appointments, Doctors, Diarys, Schedules


class AppointmentsModelTestCase(TestCase):
    """Class Testing Model Appointments """

    def setUp(self):
        """Initial Test Settings"""

        self.user = mommy.make(User)
        self.doctor = mommy.make(Doctors, name="Doutor Chapatín")
        self.diary = Diarys()
        self.diary.day = datetime.now().date()
        self.diary.doctor = self.doctor
        self.diary.save()

        schedule = Schedules()
        for h in range(1, 5):
            schedule = Schedules()
            schedule.hour = f'{h:02d}:00'
            schedule.diary = self.diary
            schedule.save()

        self.appointment = mommy.prepare(Appointments)
        self.appointment.user = self.user
        self.appointment.schedule = schedule
        self.appointment.day = schedule.diary.day
        self.appointment.doctor = schedule.diary.doctor
        self.appointment.save()

    def tearDown(self):
        """Final method"""

        Doctors.objects.all().delete()
        Diarys.objects.all().delete()
        Schedules.objects.all().delete()
        Appointments.objects.all().delete()

    def test_there_are_fields(self):
        """test the fields the model"""
        fields = ['user', 'schedule', 'date_appointment', 'day', 'doctor']

        for field in fields:
            self.assertTrue(field in dir(
                Appointments), f'Model "Appointments" does not have the field "{field}"')

    def test_there_are_appointments_creation(self):
        """test if you are creating a Appointments correctly"""

        self.assertEquals(Appointments.objects.count(), 1)
        appointment = Appointments.objects.all()[0]
        self.assertEquals(appointment.user, self.appointment.user)
        self.assertEquals(appointment.schedule, self.appointment.schedule)
        self.assertEquals(appointment.date_appointment,
                          self.appointment.date_appointment)
        self.assertEquals(appointment.day, self.appointment.day)
        self.assertEquals(appointment.doctor, self.appointment.doctor)

    def test_str_appointment(self):
        """test if str method of Appointments is correctly"""
        self.assertEquals(
            str(self.appointment), f'{self.appointment.user.username} - {self.appointment.doctor} - {self.appointment.day} {self.appointment.schedule}')
