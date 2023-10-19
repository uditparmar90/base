from django.db import models

# Create your models here.

class profile(models.Model):
    email=models.EmailField(max_length=45)
    full_name=models.CharField(max_length=30)
    date_of_birth=models.DateField()

