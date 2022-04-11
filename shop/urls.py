from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('services', views.services,name='services'),
    path('ppc', views.ppc,name='ppc'),
    path('seo', views.seo,name='seo'),
    path('webdesign', views.webdesign,name='webdesign'),
    path('webdevelopement', views.webdevelopement,name='webdevelopement'),
    path('marketing', views.marketing,name='marketing'),








]