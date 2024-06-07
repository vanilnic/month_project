from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),

    path('offers/', views.offers, name='offers'),
    path('offers/<city>/<arrival>/<departure>/<people>/', views.offers, name='offers_city'),
    path('favorites/', views.favorites, name='favorites'),
    path('travel_history/', views.travel_history, name='travel_history'),
    path('hotel/', views.hotel, name='hotel'),
    path('hotel/<id_hotel_id>/', views.hotel, name='hotel_id'),
    path('make_an_order/', views.order, name='order'),
    path('payment/', views.payments, name='payment'),
    path('successful_payment/', views.successful_payment, name='succefilly'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('favorites/<title>/', views.favorites, name='favorite'),
    path('favorites/<title>/<id_hotel_id>/<filter>/', views.favorites, name='favorite_hotel'),
    path('favorites/<title>/<city>/<arrival>/<departure>/<people>/<filter>/', views.favorites, name='favorite_offers'),
    path('travel_history/<title>/', views.travel_history, name='travels_history'),
]