from django.test import TestCase

# Create your tests here.
from rest_framework import serializers
from .models import Coordonnee

class VotreModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordonnee
        fields = '__all__'

