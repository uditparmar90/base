from django.shortcuts import render
from base.settings import BASE_DIR
from .models import product

# Create your views here.

def index(request):
    products=product.objects.all()
    return render(request,'products/home.html',{"context":products, "BASE_DIR":BASE_DIR})

def signup(request):
    return render(request,'products/signup.html')

def procuct_cat(request,product):
    print(product)
    context={"product":product}
    print(context)
    return render(request,'products/product.html',context)
