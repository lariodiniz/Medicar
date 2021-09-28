import json
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from model_mommy import mommy
from django.contrib.auth.models import User

from core.models import Specialties


class SpecialtiesViewTestCase(APITestCase):
    """test user SpecialtiesView"""

    def setUp(self):
        self.username = 'Mariguella'
        self.password = "@123@456Te7"
        self.url = reverse('core:specialties')
        self.user = mommy.prepare(User)
        self.user.username = self.username
        self.user.set_password(self.password)
        self.user.save()

        self.client = APIClient()

    def tearDown(self):
        User.objects.all().delete()
        Specialties.objects.all().delete()

    def test_specialties_view_url(self):
        """check if the endpoint 'core:specialties' is correct"""
        self.assertEqual(self.url, '/especialidades/',
                         f'a url "{self.url}" should be /especialidades/.')

    def test_specialties_view_get_user_not_login(self):
        """tests whether a get to the specialties_view of a user who is not logged in returns status 403
        """
        status_code = 403
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status_code,
                          f'a get request for url "{self.url}" is not returning status code {status_code}')
        resp = json.loads(response.content)
        self.assertEqual('detail' in resp, True,
                         f'a get request for url "{self.url}" not has detail in resp.')

    def test_specialties_view_get_user_login(self):
        """tests if a get for specialties_view returns a list of specialties correctly
        """
        status_code = 200

        for n in range(5):
            user = mommy.make(Specialties)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, status_code,
                          f'a get request for url "{self.url}" is not returning status code {status_code}')

        resp = json.loads(response.content)
        self.assertEquals(
            len(resp), 5, f'a get request for url "{self.url}" is not returning 5 registers')
        specialties = resp[0]
        self.assertEqual(type(specialties['nome']), str,
                         f'a get request for url "{self.url}" not has return correctly .')

    def test_specialties_view_get_user_login_with_filter(self):
        """tests if a get for specialties_view returns a list of specialties correctly
        """
        status_code = 200
        speci = ['Pediatria', 'Ginecologia', 'Cardiologia', 'Clínico Geral']
        for s in speci:
            mommy.make(Specialties, name=s)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url+'?search=ped')

        self.assertEquals(response.status_code, status_code,
                          f'a get request for url "{self.url}" is not returning status code {status_code}')

        resp = json.loads(response.content)
        self.assertEquals(
            len(resp), 1, f'a get request for url "{self.url}" is not returning 5 registers')
        specialties = resp[0]
        self.assertEqual(type(specialties['nome']), str,
                         f'a get request for url "{self.url}" not has return correctly .')
        self.assertEqual(specialties['nome'], 'Pediatria',
                         f'a get request for url "{self.url}" not has return correctly .')
