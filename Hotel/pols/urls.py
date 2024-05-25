from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('offers/', views.offers, name='offers'),
    path('favorites/', views.favorites, name='favorites'),
    path('travel_history/', views.travel_history, name='travel_history')
]