from rest_framework import serializers
from core.models import Diarys
from core.serializers import DoctorsSerializer, SchedulesSerializer


class DiarysSerializer(serializers.ModelSerializer):
    medico = DoctorsSerializer(read_only=True, source='doctor')
    dia = serializers.DateField(source='day')
    horarios = serializers.StringRelatedField(many=True, source='schedules')

    #horarios = serializers.ListField(many=True, source='schedules')

    # def get_horarios(self, obj):
    #    print(obj)
    #    return obj

    class Meta:
        model = Diarys
        fields = ('id', 'medico', 'dia', 'horarios')
