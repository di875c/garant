from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Catalog, Product, Gallery


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['id', 'catalog_name', 'catalog_link']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_name']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'products']