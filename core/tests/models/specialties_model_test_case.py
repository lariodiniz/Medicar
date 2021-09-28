from django.test import TestCase
from model_mommy import mommy
from core.models import Specialties


class SpecialtiesModelTestCase(TestCase):
    """Class Testing Model Specialties """

    def setUp(self):
        """Initial Test Settings"""
        self.specialties_name = 'CARDIOLOGIA'
        self.specialties = mommy.make(Specialties, name=self.specialties_name)

    def tearDown(self):
        """Final method"""
        Specialties.objects.all().delete()

    def test_there_are_fields(self):
        """test the fields the model"""

        fields = ['name']

        for field in fields:
            self.assertTrue(field in dir(
                Specialties), f'Model "Specialties" does not have the field "{field}"')

    def test_there_are_specialties_creation(self):
        """test if you are creating a Specialties correctly"""

        self.assertEquals(Specialties.objects.count(), 1)
        specialties = Specialties.objects.get(name=self.specialties_name)
        self.assertEquals(specialties.name, self.specialties.name)

    def test_str_specialties(self):
        """test if str method of Specialties is correctly"""
        self.assertEquals(str(self.specialties), f'{self.specialties.name}')
