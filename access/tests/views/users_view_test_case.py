import json
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User


class UserViewTestCase(APITestCase):
    """test user view"""

    def setUp(self):
        self.url = reverse('users:create')
        self.client = APIClient()

    def tearDown(self):
        User.objects.all().delete()

    def test_user_view_url(self):
        self.assertEqual(self.url, '/users/',
                         f'a url "{self.url}" should be /users/.')

    def test_create_view_get(self):
        """tests whether a post to creat_user_view creates a user correctly 
        """
        status_code = 201

        password = "@123@456Te7"
        new_user = {
            "username": "CheGuevara",
            "email": 'teste@teste.com.br',
            "password": password
        }

        response = self.client.post(self.url, new_user)

        resp = json.loads(response.content)
        self.assertEquals(response.status_code, status_code,
                          f'a post request for url "{self.url}" is not returning status code {status_code}')

        self.assertEqual(type(resp['username']), str,
                         f'a post request for url "{self.url}" not has return correctly .')
        self.assertEqual(type(resp['email']), str,
                         f'a post request for url "{self.url}" not has return correctly .')

        user_created = User.objects.get(username="CheGuevara")
        self.assertEquals(user_created.email, "teste@teste.com.br",
                          f'a post request for url "{self.url}" is not create a user')
        self.assertTrue(user_created.check_password(
            password), f'a post request for url "{self.url}" is not create a user')

    def test_login_view_post_error_json(self):
        user = {
            "username": "teste",
        }

        response = self.client.post(self.url, user, format='json')
        self.assertEquals(response.status_code, 400,
                          'a post request for url "{}" with wrong user is not returning status code 400'.format(self.url))
