from django.urls import path
from .views import insertBus, recherche_itineraire, insertCoordonnee


urlpatterns = [
    path('', recherche_itineraire, name='recherche_itineraire'),
    path('insertCoordonnee/', insertCoordonnee, name='insert_coordonnee'),
    path('insertBus/', insertBus, name='insert_bus')

    # Ajoutez d'autres URL au besoin
]
