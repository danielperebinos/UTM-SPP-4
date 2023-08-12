from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    enable = models.BooleanField(default=True)
    main_image = models.ImageField(null=True)
    price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Produs"
        verbose_name_plural = "Produse"

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    file = models.ImageField()
    enable = models.BooleanField(default=True)
    product = models.ForeignKey('product', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Imaginea produsului"
        verbose_name_plural = "Imaginile produsului"


class Producer(models.Model):
    company = models.CharField(max_length=250)
    contact = models.ForeignKey('contacts', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Producator"
        verbose_name_plural = "Producatori"

    def __str__(self):
        return self.company


class Contacts(models.Model):
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=12, null=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacte"

    def __str__(self):
        return f'Email: {self.email}; Phone: {self.phone}'
