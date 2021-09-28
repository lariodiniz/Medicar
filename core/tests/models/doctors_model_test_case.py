from django.test import TestCase
from model_mommy import mommy
from core.models import Doctors, Specialties


class DoctorsModelTestCase(TestCase):
    """Class Testing Model Doctors """

    def setUp(self):
        """Initial Test Settings"""
        self.specialtie_name = 'CARDIOLOGIA'
        self.specialtie = mommy.make(Specialties, name=self.specialtie_name)
        self.doctor = mommy.make(Doctors, specialtie=self.specialtie)

    def tearDown(self):
        """Final method"""
        Specialties.objects.all().delete()
        Doctors.objects.all().delete()

    def test_there_are_fields(self):
        """test the fields the model"""

        fields = ['name', 'crm', 'email', 'telephone', 'specialtie']

        for field in fields:
            self.assertTrue(field in dir(
                Doctors), f'Model "Doctors" does not have the field "{field}"')

    def test_there_are_doctors_creation(self):
        """test if you are creating a Doctors correctly"""

        self.assertEquals(Doctors.objects.count(), 1)
        doctor = Doctors.objects.all()[0]
        self.assertEquals(doctor.name, self.doctor.name)
        self.assertEquals(doctor.crm, self.doctor.crm)
        self.assertEquals(doctor.email, self.doctor.email)
        self.assertEquals(doctor.telephone, self.doctor.telephone)
        self.assertEquals(doctor.specialtie.name, self.specialtie_name)

    def test_str_doctors(self):
        """test if str method of Doctors is correctly"""
        self.assertEquals(str(self.doctor), f'{self.doctor.name}')
