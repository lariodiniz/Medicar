from datetime import datetime, timedelta
import json
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from model_mommy import mommy
from django.contrib.auth.models import User

from core.models import Specialties, Doctors, Diarys, Schedules


class AppointmentsViewTestCase(APITestCase):
    """test AppointmentsView"""

    def setUp(self):
        self.username = 'Mariguella'
        self.password = "@123@456Te7"
        self.url = reverse('core:appointments')
        self.user = mommy.prepare(User)
        self.user.username = self.username
        self.user.set_password(self.password)
        self.user.save()
        
        self.doctor = mommy.make(Doctors, name="Doutor Chapatín")
        self.diary = Diarys()
        self.diary.day = datetime.now().date() + timedelta(days=1)
        self.diary.doctor = self.doctor
        self.diary.save()


        for h in range(8, 18):          
            schedule = Schedules()
            schedule.hour = f'{h:02d}:00'
            schedule.diary = self.diary
            schedule.save()

        self.client = APIClient()

    def tearDown(self):
        User.objects.all().delete()
        Specialties.objects.all().delete()
        Doctors.objects.all().delete()
        Diarys.objects.all().delete()
        Schedules.objects.all().delete()

    def test_appointment_view_url(self):
        """check if the endpoint 'core:appointments' is correct"""
        self.assertEqual(self.url, '/consultas/',
                         f'a url "{self.url}" should be /consultas/.')

    def test_appointment_view_get_user_not_login(self):
        """tests whether a get to the appointment_view of a user who is not logged in returns status 403
        """
        status_code = 403
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status_code,
                          f'a get request for url "{self.url}" is not returning status code {status_code}')
        resp = json.loads(response.content)
        self.assertEqual('detail' in resp, True,
                         f'a get request for url "{self.url}" not has detail in resp.')

    def test_appointment_view_get_user_login(self):
        """tests if a get for appointment_view returns a list of appointment correctly
        """
        status_code = 200

        self.client.force_authenticate(user=self.user)
        
        response = self.client.get(reverse('core:diarys'))
        resp = json.loads(response.content)
        
        agenda = resp[0]['id']
        hora =  resp[0]['horarios'][8]
        object_json =  {'agenda_id': agenda, 'horario': hora}
        
        response = self.client.post(self.url, object_json, format='json')
        
        
        response = self.client.get(self.url)
        resp = json.loads(response.content)
        self.assertEquals(response.status_code, status_code,
                          f'a get request for url "{self.url}" is not returning status code {status_code}')

        self.assertEquals(
            len(resp), 1, f'a get request for url "{self.url}" is not returning 5 registers')
        
    def test_appointment_view_post_user_login_create_appointment(self):
        """tests if a get for appointment_view returns a list of appointment correctly
        """
        status_code = 200
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('core:diarys'))
        resp = json.loads(response.content)
        
        agenda = resp[0]['id']
        hora =  resp[0]['horarios'][8]
        object_json =  {'agenda_id': agenda, 'horario': hora}
        self.assertEquals(response.status_code, status_code,
                          f'a get request for url "{self.url}" is not returning status code {status_code}')

        response = self.client.post(self.url, object_json, format='json')
        resp = json.loads(response.content)
        
        self.assertEquals(response.status_code, status_code,
                          f'a post request for url "{self.url}" is not returning status code {status_code}')
