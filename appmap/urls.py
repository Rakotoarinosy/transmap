from django.urls import path
from .views import insertBus, insertChemin, recherche_itineraire, insertCoordonnee, rechercheBus


urlpatterns = [
    path('', recherche_itineraire, name='recherche_itineraire'),
    path('insertCoordonnee/', insertCoordonnee, name='insert_coordonnee'),
    path('insertBus/', insertBus, name='insert_bus'),
    path('insertChemin/', insertChemin, name='insert_chemin'),
    path('rechercheBus/', rechercheBus, name='recherche_bus')

    # Ajoutez d'autres URL au besoin
]
