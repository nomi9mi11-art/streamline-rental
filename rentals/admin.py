from django.contrib import admin

# Register your models here.
#from django.contrib import admin
from .models import CarCategory, Car, Customer, Booking, Payment

admin.site.register(CarCategory)
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Payment)
