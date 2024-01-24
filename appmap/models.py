from django.db import models

# Create your models here.
class Itineraire(models.Model):
    point_depart = models.CharField(max_length=100)
    point_arrivee = models.CharField(max_length=100)