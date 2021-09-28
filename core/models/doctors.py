from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Doctors(models.Model):
    """Doctors table model.
    Attributes:
        - name -> doctor's name
        - crm -> Doctor number on the regional council of medicine
        - email -> doctor's email
        - telephone -> doctor's phone
        - specialtie -> doctor's specialty (ForeyKey)

    """
    name = models.CharField('Nome', max_length=200)
    crm = models.CharField('CRM', max_length=200)
    email = models.EmailField('E-mail', blank=True, null=True)
    telephone = PhoneNumberField('Telefone', blank=True, null=True)
    specialtie = models.ForeignKey(
        'core.Specialties', verbose_name='Especialidade', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

    def __str__(self):
        return f'{self.name}'
