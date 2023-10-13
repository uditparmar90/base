from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class Shirts(models.Model):
    name= models.CharField(max_length=200)
    price = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )
