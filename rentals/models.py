from django.db import models

# Category of Cars (SUV, Sedan, etc.)
class CarCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Car Table
class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model_year = models.IntegerField()
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE)
    rent_per_day = models.IntegerField()
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Customer Table
class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    cnic = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


# Booking Table
class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_amount = models.IntegerField()
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return f"Booking: {self.car.name} by {self.customer.full_name}"


# Payment Table
class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount_paid = models.IntegerField()
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Booking {self.booking.id}"
