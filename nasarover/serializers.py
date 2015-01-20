from django.forms import widgets
from rest_framework import serializers
from nasarover.models import Rover
class RoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rover
        fields = ('user_id','rover_name')
