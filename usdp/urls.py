from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='main'),
    path("our_cars/", views.our_cars, name='our_cars'),
    path("calculator/", views.calculator, name='calculator'),
    path("contacts/", views.contacts, name='contacts'),
    path("our_car/<str:title>", views.our_car, name='our_car'),
    path("services/", views.services, name='services'),
    path('modal_form/', views.modal_form, name='modal_form'),
    path('result/<str:auction_type>/'
         '<str:fuel_type>/'
         '<str:engine_field>/'
         '<int:year>/'
         '<int:auction_price>/'
         '<int:age>/'
         '<str:selected_location>/'
         '<int:shipping_ocean>/'
         '<int:shipping_USA>', views.result, name='result')

    # path('result/<str:auction_type>/'
    #      '<str:fuel_type>/'
    #      '<int:auction_price>/'
    #      '<str:engine_field>/'
    #      '<int:year>/'
    #      '<int:engine_tax>'
    #      '<str:selected_location>/'
    #      '<int:auction_tax>/'
    #      '<int:shipping_ocean>/'
    #      '<int:shipping_USA>/'
    #      '<int:shipping_to_europe>/'
    #      '<int:import_duty>/'
    #      '<int:vat>/'
    #      '<int:shipping_services>/'
    #      '<int:brokerage_services>/'
    #      , views.result, name='result')
    ]