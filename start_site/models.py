from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db import models


class Catalog(models.Model):
    catalog_name = models.CharField(max_length=56, blank=False)
    catalog_link = models.CharField(max_length=56, blank=False, null=False)
    catalog_image = models.ImageField(upload_to='catalogs/', null=True, blank=True)
    catalog_description = models.TextField(max_length=512, blank = True)

    def __str__(self):
        return f"{self.catalog_name}"


class Product(models.Model):
    # catalog = models.ForeignKey(Catalog, related_name='products', on_delete=models.CASCADE)
    catalog = models.ManyToManyField(Catalog, related_name='product')
    item_name = models.CharField(max_length=32, blank=False)
    item_image = models.ImageField(upload_to='items/img/%Y-%m-%d/', null=False, blank=False)
    item_description = models.TextField(max_length=1512, blank=True)

    def __str__(self):
        return f"{self.item_name}"


class Gallery(models.Model):
    products = models.ForeignKey(Product, related_name='gallery', on_delete=models.CASCADE)
    item_image = models.ImageField(upload_to='gallery/img/%Y-%m-%d/', null=False, blank=False)
    item_description = models.TextField(max_length=1512, blank=True)

    def __str__(self):
        return f"{self.products}"
