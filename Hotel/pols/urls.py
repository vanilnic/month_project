from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('offers/', views.offers, name='offers'),
    path('favorites/', views.favorites, name='favorites'),
    path('travel_history/', views.travel_history, name='travel_history'),
    path('hotel/', views.hotel, name='hotel'),
    path('make_an_order/', views.order, name='order'),
    path('payment/', views.payments, name='payment'),
    path('successful_payment/', views.successful_payment, name='succefilly'),
    # path('', views.registrarion, name='registration')
]