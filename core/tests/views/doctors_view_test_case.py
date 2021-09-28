import json
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from model_mommy import mommy
from django.contrib.auth.models import User

from core.models import Specialties, Doctors


class DoctorsViewTestCase(APITestCase):
    """test user DoctorsView"""

    def setUp(self):
        self.username = 'Mariguella'
        self.password = "@123@456Te7"
        self.url = reverse('core:doctors')
        self.user = mommy.prepare(User)
        self.user.username = self.username
        self.user.set_password(self.password)
        self.user.save()

        self.client = APIClient()

    def tearDown(self):
        User.objects.all().delete()
        Specialties.objects.all().delete()
        Doctors.objects.all().delete()

    def test_dotors_view_url(self):
        """check if the endpoint 'core:doctors' is correct"""
        self.assertEqual(self.url, '/medicos/',
                         f'a url "{self.url}" should be /medicos/.')

    def test_dotors_view_get_user_not_login(self):
        """tests whether a get to the dotors_view of a user who is not logged in returns status 403
        """
        status_code = 403
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status_code,
                          f'a get request for url "{self.url}" is not returning status code {status_code}')
        resp = json.loads(response.content)
        self.assertEqual('detail' in resp, True,
                         f'a get request for url "{self.url}" not has detail in resp.')

    def test_dotors_view_get_user_login(self):
        """tests if a get for dotors_view returns a list of doctors correctly
        """
        status_code = 200

        for n in range(5):
            s = mommy.make(Specialties)
            user = mommy.make(Doctors, specialtie=s)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, status_code,
                          f'a get request for url "{self.url}" is not returning status code {status_code}')

        resp = json.loads(response.content)
        self.assertEquals(
            len(resp), 5, f'a get request for url "{self.url}" is not returning 5 registers')
        doctors = resp[0]
        self.assertEqual(type(doctors['id']), int,
                         f'a get request for url "{self.url}" not has return correctly .')
        self.assertEqual(type(doctors['crm']), str,
                         f'a get request for url "{self.url}" not has return correctly .')
        self.assertEqual(type(doctors['nome']), str,
                         f'a get request for url "{self.url}" not has return correctly .')
        self.assertEqual(type(doctors['especialidade']), dict,
                         f'a get request for url "{self.url}" not has return correctly .')

    def test_dotors_view_get_user_login_with_filter(self):
        """tests if a get for dotors_view returns a list of doctors correctly
        """
        status_code = 200
        speci = ['Pediatria', 'Ginecologia', 'Cardiologia', 'Clínico Geral']
        name = ['Drauzio Varella', 'Gregory House',
                'Tony Tony Chopper', 'Chapatins']
        for k, n in enumerate(name):
            s = mommy.make(Specialties, name=speci[k])
            mommy.make(Doctors, name=n, specialtie=s)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            self.url+'?search=drauzio&especialidade=1&especialidade=3')

        self.assertEquals(response.status_code, status_code,
                          f'a get request for url "{self.url}" is not returning status code {status_code}')

        resp = json.loads(response.content)
        self.assertEquals(
            len(resp), 1, f'a get request for url "{self.url}" is not returning 5 registers')
        doctors = resp[0]
        self.assertEqual(type(doctors['nome']), str,
                         f'a get request for url "{self.url}" not has return correctly .')
        self.assertEqual(doctors['nome'], 'Drauzio Varella',
                         f'a get request for url "{self.url}" not has return correctly .')
        self.assertEqual(doctors['especialidade']['nome'], 'Pediatria',
                         f'a get request for url "{self.url}" not has return correctly .')
