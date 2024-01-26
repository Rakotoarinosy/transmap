# Create your tests here.
from rest_framework import serializers
from .models import Bus, Coordonnee, chemin

class CoordonneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordonnee
        fields = '__all__'
        
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'
        
class CheminSerialiser(serializers.ModelSerializer):
    class Meta:
        model = chemin
        fields = '__all__'