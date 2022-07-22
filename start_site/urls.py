from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', csrf_exempt(views.MainPage.as_view())),
    path('error/', csrf_exempt(views.ErrorView.as_view())),
    re_path(r'catalog/(?P<catalog_link>[a-z]+)', csrf_exempt(views.CatalogView.as_view())),
    path('contacts/', csrf_exempt(views.ContactView.as_view())),
    path('gallery/', csrf_exempt(views.GalleryView.as_view())),
    # path('test/', csrf_exempt(views.TestView.as_view())),
]