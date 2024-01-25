from django.urls import path
from .views import recherche_itineraire

urlpatterns = [
    path('', recherche_itineraire, name='recherche_itineraire'),
    # Ajoutez d'autres URL au besoin
]
