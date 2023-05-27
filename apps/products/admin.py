from django.contrib import admin
from apps.products.models import Product, ProductImage, Producer, Contacts

admin.site.register([Product, ProductImage, Producer, Contacts])
# Register your models here.
