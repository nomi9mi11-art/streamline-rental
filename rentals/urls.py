from django.urls import path
from . import views
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", views.home, name="home"),
    path("cars/", views.cars_list, name="cars_list"),
    path("cars/<int:car_id>/", views.car_detail, name="car_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("", include("rentals.urls")),
    path('admin/', admin.site.urls),
]
