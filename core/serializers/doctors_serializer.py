from rest_framework import serializers
from core.models import Doctors
from core.serializers import SpecialtiesSerializer


class DoctorsSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='name')
    especialidade = SpecialtiesSerializer(read_only=True, source='specialtie')

    class Meta:
        model = Doctors
        fields = ('id', 'crm', 'nome', 'especialidade')
