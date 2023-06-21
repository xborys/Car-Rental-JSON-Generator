from django.contrib import admin
from .models import Client, Employee, Car_Type, Car, Reservation, Rent, Rental_issue, Rental_return, Rental_bill, Car_status

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Car_Type)
admin.site.register(Car)
admin.site.register(Reservation)
admin.site.register(Rent)
admin.site.register(Rental_issue)
admin.site.register(Rental_return)
admin.site.register(Rental_bill)
admin.site.register(Car_status)


