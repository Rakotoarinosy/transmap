import requests
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Coordonnee  # Remplacez 'VotreModele' par le nom de votre modèle
from .serializers import BusSerializer, CoordonneeSerializer


@api_view(['GET'])
def recherche_itineraire(request):
    return Response({'message': 'Hello, world!'})



@api_view(['POST'])
def insertCoordonnee(request):
    if request.method == 'POST':
        data = request.data.get('coordonne')
        print(data)
        errors = []
        for value in data:
            serializer = CoordonneeSerializer(data=value)
            if serializer.is_valid():
                serializer.save()
            else:
                errors.append({value: serializer.errors})
        
        if errors:
            return Response({'errors': errors}, status=400)
        else:
            return Response({'message': 'Données insérées avec succès'}, status=201)
    else:
        return Response({'message': 'Méthode non autorisée'}, status=405)

@api_view(['POST'])
def insertBus(request):
    if request.method == 'POST':
        try:
            serializer = BusSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Données insérées avec succès'}, status=201)
            else:
                return Response({'errors': serializer.errors}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    else:
        return Response({'message': 'Méthode non autorisée'}, status=405)