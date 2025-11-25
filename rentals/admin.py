from django.contrib import admin
from .models import CarCategory, Car, Customer, Booking, Payment


@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'model_year', 'rent_per_day', 'is_available', 'category']
    list_filter = ['is_available', 'category', 'brand']
    search_fields = ['name', 'brand']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'email', 'cnic']
    search_fields = ['full_name', 'cnic', 'phone']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['car', 'customer', 'start_date', 'end_date', 'total_amount', 'status']
    list_filter = ['status', 'start_date']
    search_fields = ['car__name', 'customer__full_name']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['booking', 'amount_paid', 'payment_date']
    readonly_fields = ['payment_date']

admin.site.site_header = "Streamline Rental Admin"
admin.site.site_title = "Streamline Rental"
admin.site.index_title = "Welcome to Streamline Rental Dashboard"
