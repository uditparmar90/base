from django.contrib import admin
from .models import Shirt
from.models import product

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("slug","name")
    list_display=("name","id", "category","image","brand","price","is_bestseller")
    list_filter=("is_bestseller",)
    search_fields=("name","category","brand")

# Register models here.
admin.site.register(Shirt)
admin.site.register(product,ProductAdmin)

