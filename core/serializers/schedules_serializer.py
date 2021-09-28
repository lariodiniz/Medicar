from rest_framework import serializers
from core.models import Schedules


class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = ['start']
