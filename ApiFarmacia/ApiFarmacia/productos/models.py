from django.db import models

class Productos(models.Model):
    id_pro = models.IntegerField(primary_key=True)
    nom_pro = models.CharField(max_length=30)
    stock = models.IntegerField()

