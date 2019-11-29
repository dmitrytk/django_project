from django.urls import path

from . import views

urlpatterns = [
    path('distance/', views.distance, name='distance'),
    path('sub/', views.sub, name='sub'),
    path('water/', views.water, name='water'),
    path('print/', views.prn, name='print'),
    path('roxar/', views.roxar, name='roxar'),
]
