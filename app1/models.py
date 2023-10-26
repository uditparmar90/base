from django.db import models
from django.core.validators import MinValueValidator



# Create your models here.

class Shirt(models.Model):
    name= models.CharField(max_length=200)
    price = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )
    # null=True == means that the database will allow the field to have no value, essentially representing an empty or missing value in the database.
    brand=models.CharField(max_length=15,null=True)
    # empty=True == means that the field is not required when submitting data through a form. You can submit a form with that field left empty.
    description=models.CharField(max_length=200,blank=True)
    is_bestseller = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}"
    
class Brand(models.Model):
    title=models.CharField(max_length=20)
    logo=models.ImageField(blank=True)


class product(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    category=models.CharField(max_length=10)
    image=models.ImageField(blank=True, upload_to="product-img")
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.CASCADE)
    price=models.IntegerField(
        validators=[MinValueValidator(0.0)]
    )
    slug=models.SlugField(blank=True)
    is_bestseller=models.BooleanField(blank=True,default=False)


    def __str__(self):
        return f"{self.name}"
    
    def save(self,*args,**kwargs):
        super(product,self).save(*args,**kwargs)
        self.slug=self.id
        super(product,self).save(*args,**kwargs)


