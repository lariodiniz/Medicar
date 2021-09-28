from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

from core.models import Appointments, Schedules
from core.serializers import AppointmentsSerializer


class AppointmentsView(ListAPIView):
    """Lists the appointments."""
    queryset = Appointments.objects.all().order_by('day', 'schedule__hour')
    serializer_class = AppointmentsSerializer

    def get_queryset(self):

        user = self.request.user
        queryset = Appointments.objects.filter(
            user=user, day__gte=datetime.now().date(), schedule__hour__gte=datetime.now().time()).order_by('day', 'schedule__hour')
        return queryset

    def _valid_json(self, data):
        fields = data.keys()

        retorno = {}
        if (not 'agenda_id' in fields):
            retorno['agenda_id'] = ["Este campo é obrigatório."]

        if (not 'horario' in fields):
            retorno['horario'] = ["Este campo é obrigatório."]
        retorno['horario'] = ["Este campo é obrigatório."]
        if (not 'agenda_id' in fields or
                not 'horario' in fields):
            return True, retorno

        return False, ''

    def post(self, request, format='json'):
        error, mens = self._valid_json(request.data)
        if error:
            return Response(data=mens, status=status.HTTP_400_BAD_REQUEST)
        else:

            try:
                schedule = Schedules.objects.get(
                    diary__id=request.data['agenda_id'],
                    hour=request.data['horario'],
                    hour__gte=datetime.now().time(),
                    diary__day__gte=datetime.now().date(),
                    appointment=None)
            except Schedules.DoesNotExist:
                raise Http404

            if Appointments.objects.filter(user=request.user,
                                           day=schedule.diary.day,
                                           schedule__hour=request.data['horario']

                                           ).exists():
                raise Http404
            else:
                appointment = Appointments()
                appointment.user = request.user
                appointment.schedule = schedule
                appointment.day = schedule.diary.day
                appointment.doctor = schedule.diary.doctor
                appointment.save()

                serializer = AppointmentsSerializer(appointment)
                return Response(serializer.data, status=status.HTTP_200_OK)
