from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime


def validate_date_pass(value):
    if value < datetime.now().date():
        raise ValidationError(
            "Selected day already past!")


class Diarys(models.Model):
    """Diarys table model.
    Attributes:
        - day -> Physician's Allocation Date
        - doctor -> doctor (ForeyKey)
    """
    day = models.DateField('Data', validators=[validate_date_pass])
    doctor = models.ForeignKey(
        'core.Doctors', verbose_name='Medico', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.day < datetime.now().date():
            raise ValidationError(
                "Selected day already past!")
        elif Diarys.objects.filter(doctor=self.doctor, day=self.day).exists():
            raise ValidationError(
                "There is already an agenda on that day for this doctor!")
        else:
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self):
        return f'{self.doctor.name} - {self.day}'
