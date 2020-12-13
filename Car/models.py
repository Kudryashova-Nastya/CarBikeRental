from django.db import models

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=100)
    metro = models.CharField(max_length=30)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=10)
class Car_model(models.Model):
    name = models.CharField(max_length=100)
    gearbox = models.CharField(max_length=15)
    body = models.CharField(max_length=15)
    seats = models.PositiveSmallIntegerField()
    drive = models.CharField(max_length=10)
    engine = models.CharField(max_length=10)
    doors = models.PositiveSmallIntegerField()
    rudder = models.CharField(max_length=6)


class Car(models.Model):
    car_id = models.CharField(max_length=100)
    car_model_id = ForeignKey(Car_model, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    location_id = ForeignKey(Location, on_delete=models.CASCADE)
    casco = models.BooleanField()
    osago = models.BooleanField()
    max_limit = models.PositiveSmallIntegerField()
    mileage = PositiveIntegerField()
    color = models.CharField(max_length=20)
    number = models.CharField(max_length=10)
    photo = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
