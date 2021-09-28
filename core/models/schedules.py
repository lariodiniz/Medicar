from django.db import models
from django.core.validators import MaxValueValidator


class Schedules(models.Model):
    """Schedules table model.
    Attributes:
        - hour -> schedule start time
        - minute -> starting minute of the schedule
    methods:
        - start -> return schedule start time in stringformat
        - finish -> return schedule finish time in stringformat

    """
    hour = models.TimeField('Hora', auto_now=False, auto_now_add=False)
    diary = models.ForeignKey(
        'core.Diarys', verbose_name='Agenda', on_delete=models.CASCADE, related_name='schedules')

    @property
    def finish(self):
        hour_finish = self.hour + 1
        return f'{hour_finish}'

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        hour = str(self.hour).split(':')
        return f'{hour[0]}:{hour[1]}'

