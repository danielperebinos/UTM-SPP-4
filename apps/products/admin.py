from django.contrib import admin
from django.utils.html import format_html

from apps.products.models import Product, ProductImage, Producer, Contacts


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(
            '<img src="{}" style="max-height:100px;"/>'.format(obj.main_image.url)
        )

    list_display = ["title", "enable", "image", "producer"]
    search_fields = ["title"]
    list_filter = ["enable"]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(
            '<img src="{}" style="max-height:100px;"/>'.format(obj.file.url)
        )

    list_display = ["product", "enable", "image"]
    search_fields = ["title"]


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = search_fields = ["company", "contact"]


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = search_fields = ["email", "phone"]
