from django.views import View, generic
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Catalog, Product, Gallery
from django.conf import settings
from django.core.mail import send_mail



class MainPage(View):
    def get(self, request, *args, **kwargs):
        catalogs = Catalog.objects.all()
        return render(request, 'first_page.html', {'catalogs': catalogs})

    def post(self, request, *args, **kwargs):
        try:
            email_data = request.POST
            if 'selfsend' in email_data: email_address = [email_data['email'], settings.EMAIL_HOST_USER]
            else: email_address = [settings.EMAIL_HOST_USER]
            text_email = email_data['textemail']
            text_email += '''\n телефон: {} \n адресс электронной почты: {}'''.format(email_data['phonenumber'], email_data['email'])
            headers = "Запрос от {} {} компания {}".format(email_data['name'], email_data['lastname'], email_data['companyname'])
            send_mail(headers, text_email, settings.EMAIL_HOST_USER, email_address)
            return HttpResponseRedirect('/')
        except: return HttpResponseRedirect('/error')


class CatalogView(View):
    def get(self, request, *args, **kwargs):
        catalogs = Catalog.objects.all()
        products = Catalog.objects.get(catalog_link=kwargs['catalog_link']).product.all()
        if len(products) == 0: products = []
        return render(request, 'catalog.html', {'catalogs': catalogs, 'products': products})


class ErrorView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'error_page.html')


# class TestView(View):
#     def get(self, request, *args, **kwargs):
#         catalogs = Catalog.objects.all()
#         gallery = Gallery.objects.all()
#         if len(gallery) == 0: gallery = []
#         return render(request, 'test.html', {'catalogs': catalogs, 'gallery': gallery})


class GalleryView(View):
    def get(self, request, *args, **kwargs):
        catalogs = Catalog.objects.all()
        gallery = Gallery.objects.all()
        if len(gallery) == 0: gallery = []
        return render(request, 'gallery.html', {'catalogs': catalogs, 'gallery': gallery})


class ContactView(View):
    def get(self, request, *args, **kwargs):
        catalogs = Catalog.objects.all()
        return render(request, 'contact.html', {'catalogs': catalogs})
