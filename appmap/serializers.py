# Create your tests here.
from rest_framework import serializers
from .models import Bus, Coordonnee

class CoordonneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordonnee
        fields = '__all__'
        
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'