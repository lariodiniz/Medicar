from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_date_pass(value):
    if value < datetime.now().date():
        raise ValidationError(
            "Selected day already past!")


class Appointments(models.Model):
    """Appointments table model.
    Attributes:
        - user -> user (ForeyKey)
        - schedule -> schedule (OneToOne)
        - date_appointment -> recording date. auto date.
        - day -> starting minute of the schedule
        - doctor -> doctor (ForeyKey)

    """
    user = models.ForeignKey(
        User, verbose_name='Usuario', on_delete=models.CASCADE)

    schedule = models.OneToOneField(
        'core.Schedules', verbose_name='Horario', on_delete=models.SET_NULL, null=True, related_name='appointment')

    date_appointment = models.DateTimeField(
        'Data do Agendamento', auto_now_add=True)

    day = models.DateField('Data', validators=[validate_date_pass])
    doctor = models.ForeignKey(
        'core.Doctors', verbose_name='Medico', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return f'{self.user.username} - {self.doctor} - {self.day} {self.schedule}'
