from django.db import models
from General.models import Location
from General.models import User
from General.models import Deliveryman
from General.models import Delivery

# Create your models here.

class Car_model(models.Model):
    name = models.CharField(max_length=100)
    gearbox = models.CharField(max_length=15)
    body = models.CharField(max_length=15)
    seats = models.PositiveSmallIntegerField()
    drive = models.CharField(max_length=10)
    engine = models.CharField(max_length=10)
    doors = models.PositiveSmallIntegerField()
    rudder = models.CharField(max_length=6)
    def __str__(self):
        return self.name or ''


class Car(models.Model):
    brand = models.CharField(max_length=100)
    car_model_id = models.ForeignKey(Car_model, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    casco = models.BooleanField()
    osago = models.BooleanField()
    max_limit = models.PositiveSmallIntegerField()
    mileage = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    number = models.CharField(max_length=10)
    photo = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.number or ''


class Car_rent(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    start = models.DateTimeField()
    end = models.DateTimeField()
    region =  models.CharField(max_length=40)
    delivery_to_id = models.ForeignKey(Delivery, on_delete=models.CASCADE, blank=True, null=True)
    delivery_from_id = models.ForeignKey(Delivery, on_delete=models.CASCADE, blank=True, null=True, related_name='deliveryfromcar')
    limit = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    comment = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return str(self.car_id) or ''
