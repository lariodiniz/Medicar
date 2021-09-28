from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

from core.models import Appointments, Schedules
from core.serializers import AppointmentsSerializer


class AppointmentsDeleteView(APIView):
    """delete the appointments informed"""

    def delete(self, request, appointment_id, format=None):
        try:
            appointment = Appointments.objects.get(
                id=appointment_id,
                user=request.user,
                day__gte=datetime.now().date(),
                schedule__hour__gte=datetime.now().time()

            )
        except Appointments.DoesNotExist:
            raise Http404
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
