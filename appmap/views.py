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
        # Supposons que "exemple" soit la valeur que vous souhaitez filtrer
        valeur_arret = "Mahamasina"

        # Effectuer la requête pour récupérer les coordonnées correspondantes
        coord_list = Coordonnee.objects.filter(arret=valeur_arret)

        # Initialiser une liste pour stocker les informations des bus correspondants
        bus_info_list = []

        # Parcourir chaque coordonnée
        for coord in coord_list:
            # Récupérer le chemin correspondant à la coordonnée
            chem = chemin.objects.filter(idCor=coord).first()
            
            # Vérifier si le chemin existe
            if chem:
                # Récupérer le bus correspondant au chemin
                bus_correspondant = chem.idBus
                
                if bus_correspondant:
                    # Ajouter les informations du bus à la liste
                    bus_info_list.append({
                        'arret': coord.arret,
                        'bus_nom': bus_correspondant.nom,
                        'latitude': coord.latitude,
                        'longitude': coord.longitude
                    })
                else:
                    # Ajouter un message indiquant qu'aucun bus correspondant n'a été trouvé pour cet arrêt
                    print("Aucun bus correspondant trouvé")
                    bus_info_list.append({
                        'arret': coord.arret,
                        'message': "Aucun bus correspondant trouvé"
                    })

        # Retourner la liste des informations des bus correspondants en tant que réponse
        return Response(bus_info_list)
