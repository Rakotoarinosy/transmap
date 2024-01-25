import requests
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Coordonnee  # Remplacez 'VotreModele' par le nom de votre modèle
from .serializers import CoordonneeSerializer


@api_view(['GET'])
def recherche_itineraire(request):
    return Response({'message': 'Hello, world!'})



@api_view(['POST'])
def insertCoordonnee(request):
      if request.method == 'POST':
        serializer = CoordonneeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Données insérées avec succès'}, status=201)
        return Response(serializer.errors, status=400)


