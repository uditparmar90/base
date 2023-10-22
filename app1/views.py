from django.shortcuts import render
from .models import product

# Create your views here.
def index(request):
    products=product.objects.all().order_by('-id')[:4]
    print(products)
    return render(request,'products/home.html',{"context":products,})

def signup(request):
    return render(request,'products/signup.html')

def procuct_cat(request,product):
    print(product)
    context={"product":product}
    print(context)
    return render(request,'products/product.html',context)
