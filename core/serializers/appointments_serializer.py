from rest_framework import serializers
from core.models import Appointments
from core.serializers import DoctorsSerializer


class AppointmentsSerializer(serializers.ModelSerializer):
    #nome = serializers.CharField(source='name')
    #medico = serializers.SerializerMethodField()

    # def get_medico(self, obj):
    #    print(obj)
    #    return obj.get_schedule.diary.doctor
    dia = serializers.DateField(source='day')
    medico = DoctorsSerializer(source='doctor')
    horario = serializers.StringRelatedField(source='schedule')
    data_agendamento = serializers.StringRelatedField(
        source='date_appointment')

    class Meta:
        model = Appointments
        fields = ['id', 'dia', 'horario', 'data_agendamento', 'medico']
