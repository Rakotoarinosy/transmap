from django.db import models

# Create your models here.
class Bus(models.Model):
    nom = models.CharField(max_length=30)
    
class Coordonnee(models.Model):
    label = models.CharField(max_length=250)
    longitude = models.FloatField()
    latitude = models.FloatField()
    
    def __str__(self) -> str:
        return self.label
    
class chemin(models.Model):
    idBus = models.ForeignKey(Bus, verbose_name=("relation bus"), on_delete=models.SET_NULL, null=True)
    idCor = models.ForeignKey(Coordonnee, verbose_name=("relation coordonnee"), on_delete=models.SET_NULL, null=True)