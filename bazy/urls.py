from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('export_clients_json/', views.export_clients_json, name='export_clients_json'),
    path('import_clients/', views.import_clients, name='import_clients'),
    path('generate_clients/', views.generate_clients, name='generate_clients'),
    path('employees/', views.employees, name='employees'),
    path('export-employees/', views.export_employees, name='export_employees'),
    path('import-employees/', views.import_employees, name='import_employees'),
    path('generate_employees/', views.generate_employees, name='generate_employees'),
    path('cars/', views.cars, name='cars'),
    path('export-cars/', views.export_cars, name='export_cars'),
    path('import-cars/', views.import_cars, name='import_cars'),
    path('generate_cars/', views.generate_cars, name='generate_cars'),
    path('preview_json/', views.preview_json, name='preview_json'),
    path('reservations/', views.reservations, name='reservations'),
    path('rents/', views.rents, name='rents'),
    path('rental_bill/', views.rental_bill, name='rental_bill'),
    path('rental_issue/', views.rental_issue, name='rental_issue'),
    path('rental_return/', views.rental_return, name='rental_return'),
    path('car_status/', views.car_status, name='car_status'),
    path('car_type/', views.car_type, name='car_type'),
]
