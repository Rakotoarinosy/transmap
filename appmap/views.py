import requests
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Coordonnee, chemin, Bus  # Remplacez 'VotreModele' par le nom de votre modèle
from .serializers import BusSerializer, CheminSerialiser, CoordonneeSerializer


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
    
@api_view(['GET'])
def insertChemin(request):
    coordonnees = Coordonnee.objects.all()
    serialized_coordonnees = CoordonneeSerializer(coordonnees, many=True)  # Sérialisez toutes les instances
    
    for coordonnee in serialized_coordonnees.data:
        coordonnee_id = coordonnee['id']
        print("ID:", coordonnee_id)
        data = {
            "idBus": 1,
            "idCor": coordonnee_id
        }
        try:
            serializer = CheminSerialiser(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'errors': serializer.errors}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    return Response({'message': 'Données insérées avec succès'}, status=201)

"""@api_view(['POST'])
def rechercheBus(request):
    if request.method == 'POST':
        data = request.data.get('coordonne')
        print(data)
        cords=[]
        busTest = []
        errors = []
        tabBusRep=[]
        busRep=""
        for value in data:
            coordonnees = Coordonnee.objects.all()
            serialized_coordonnees = CoordonneeSerializer(coordonnees, many=True)  # Sérialisez toutes les instances

            for coordonnee in serialized_coordonnees.data:
                if coordonnee['latitude'] == value['latitude'] and coordonnee['longitude'] == value['longitude']:
                    cords.append(coordonnee['id'])
            if errors:
                return Response({'errors': errors}, status=400)
        for cord in cords:
            chemins = chemin.objects.all()
            serialized_chemins = CheminSerialiser(chemins, many=True)
            for chem in serialized_chemins.data:
                if chem['idCor'] == cord:
                    busTest.append(chem['idBus'])
                  
        print(cords)
        # Maka anarana bus
        for busT in busTest:
            buss = Bus.objects.all()
            serialized_buss = BusSerializer(buss, many=True)  # 
            for bus in serialized_buss.data:
                if bus['id'] == busT:         
                                 
                    if len(tabBusRep) != 0:
                        isExist=False
                        for buse in tabBusRep:
                            if(bus['nom'] == buse):              #Izay miverina in-2 no sady nandalo depart no nandalo arrivee
                                busRep=busRep+buse+","
                                isExist=True
                            
                        if isExist==False :
                            tabBusRep.append(bus['nom'])
                    else:
                        tabBusRep.append(bus['nom'])

        print(tabBusRep)
        
        if busRep != "":
            print({'message': busRep})
            return Response({'message': busRep})
        else:
            print({'message': "Aucun bus"})
            return Response({'message': "Aucun bus"})
    else:
            return Response({'message': 'Méthode non autorisée'}, status=405)
        
"""
@api_view(['POST'])
def rechercheBus(request):
    if request.method == 'POST':
        # Supposons que vous recevez les points de départ et d'arrivée depuis la requête POST
        depart = request.data.get('depart', None)
        arriver = request.data.get('arrive', None)
        
        depart = depart.lower()
        arriver= arriver.lower()
        
        if depart is None or arriver is None:
            return Response({'message': 'Veuillez fournir un point de départ et un point d\'arrivée'})

        # Effectuer la requête pour récupérer les coordonnées correspondantes pour le départ et l'arrivée
        coord_depart = Coordonnee.objects.filter(label=depart).first()
        coord_arriver = Coordonnee.objects.filter(label=arriver).first()

        if coord_depart is None or coord_arriver is None:
            return Response({'message': 'Impossible de trouver les coordonnées pour le point de départ ou le point d\'arrivée'})

        # Initialiser une liste pour stocker les informations des bus correspondants
        bus_info_list = []
        bus_noms = []

        # Récupérer les chemins possibles entre le point de départ et le point d'arrivée
        chemins = chemin.objects.filter(idCor=coord_depart) and chemin.objects.filter(idCor=coord_arriver)

        print('Chemins :', chemins)
        
        # Parcourir chaque chemin
        for chem in chemins:
            # Récupérer le bus correspondant au chemin
            bus_correspondant = chem.idBus

            if bus_correspondant:
                # Ajouter les informations du bus à la liste
                bus_info_list.append({
                    'arret_depart': coord_depart.label,
                    'arret_arriver': coord_arriver.label,
                    'bus_nom': bus_correspondant.nom,
                    'latitude_depart': coord_depart.latitude,
                    'longitude_depart': coord_depart.longitude,
                    'latitude_arriver': coord_arriver.latitude,
                    'longitude_arriver': coord_arriver.longitude
                })

        bus_noms.clear()
        # Parcourir chaque dictionnaire dans la liste
        for bus_info in bus_info_list:
            # Extraire la valeur associée à la clé 'bus_nom'
            bus_nom = bus_info['bus_nom']
            # Ajouter la valeur extraite à la liste bus_noms
            bus_noms.append(bus_nom)

        # Afficher la liste des valeurs de bus_nom
        print(bus_noms)
            
        # Retourner la liste des informations des bus correspondants en tant que réponse
        print(bus_info_list)
        return Response(bus_info_list)

