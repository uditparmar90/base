from django.contrib import admin
from .models import Shirt
from.models import product

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)

# Register models here.
admin.site.register(Shirt)
admin.site.register(product,ProductAdmin)

