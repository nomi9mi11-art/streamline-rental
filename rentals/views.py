from django.shortcuts import render
from .models import Car   # agar model ka naam Car hai

def home(request):
    cars = Car.objects.all()[:3]  # Featured cars
    return render(request, "rentals/home.html", {"cars": cars})

def cars_list(request):
    cars = Car.objects.all()
    return render(request, "rentals/cars.html", {"cars": cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, "rentals/car_detail.html", {"car": car})

def about(request):
    return render(request, "rentals/about.html")

def contact(request):
    return render(request, "rentals/contact.html")
