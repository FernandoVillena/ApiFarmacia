from django.db import models
from ApiFarmacia.utils import max_min_validator

class Productos(models.Model):
    id_pro = models.IntegerField(primary_key=True)
    nom_pro = models.CharField(max_length=30)
    stock = models.IntegerField(validators=[max_min_validator])

