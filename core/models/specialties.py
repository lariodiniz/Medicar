from django.db import models


class Specialties(models.Model):
    """Specialties table model.
    Attributes:
        - name ->name of medical specialty
    """
    name = models.CharField('Nome', max_length=200)

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return f'{self.name}'
