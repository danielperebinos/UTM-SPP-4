from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250, null=False)
    description = models.TextField()
    enable = models.BooleanField(default=True, null=False)
    main_image = models.ImageField(null=True)
    price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # producator = models.ForeignKey('Producer', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Produs"
        verbose_name_plural = "Produse"

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    file = models.ImageField(null=False)
    enable = models.BooleanField(default=True, null=False)
    product = models.ForeignKey('product', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Imaginea produsului"
        verbose_name_plural = "Imaginile produsului"


class Producer(models.Model):
    company = models.CharField(max_length=250, null=False)
    contact = models.ForeignKey('contacts', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Producator"
        verbose_name_plural = "Producatori"


class Contacts(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=12)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacte"
