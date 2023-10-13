from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'products/home.html')

def signup(request):
    return render(request,'products/signup.html')

def procuct_cat(request,product):
    print(product)
    context={"product":"product"}
    print(context)
    return render(request,'products/product.html',context)
