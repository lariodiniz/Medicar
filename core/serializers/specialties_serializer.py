from rest_framework import serializers
from core.models import Specialties


class SpecialtiesSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='name')

    class Meta:
        model = Specialties
        fields = ['id', 'nome']
