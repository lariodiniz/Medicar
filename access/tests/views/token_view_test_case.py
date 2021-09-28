import json
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from model_mommy import mommy


class TokenViewTestCase(APITestCase):
    """test TokenView view"""

    def setUp(self):
        self.username = 'Mariguella'
        self.password = "@123@456Te7"
        self.url = reverse('users:token')
        self.user = mommy.prepare(User)
        self.user.username = self.username
        self.user.set_password(self.password)
        self.user.save()

        self.client = APIClient()

    def test_token_view_url(self):
        self.assertEqual(self.url, '/users/login',
                         f'a url "{self.url}" should be /users/login.')

    def tearDown(self):
        User.objects.all().delete()

    def test_token_view_get(self):
        """tests whether a post to token_view return a token correctly 
        """
        status_code = 200

        user = {
            "username": self.username,
            "password": self.password
        }

        response = self.client.post(self.url, user)

        resp = json.loads(response.content)
        self.assertEquals(response.status_code, status_code,
                          f'a post request for url "{self.url}" is not returning status code {status_code}')

        self.assertEqual(type(resp['token']), str,
                         f'a post request for url "{self.url}" not has return correctly .')

    def test_token_view_post_error_json(self):
        user = {
            "username": "teste",
            "password": "teste",
        }

        response = self.client.post(self.url, user, format='json')
        self.assertEquals(response.status_code, 400,
                          'a post request for url "{}" with wrong user is not returning status code 400'.format(self.url))
