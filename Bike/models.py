from django.db import models

from General.models import Location
from General.models import User
from General.models import Deliveryman
from General.models import Delivery

# Create your models here.

class Bike_model(models.Model):
    name = models.CharField(max_length=100)
    type_bike = models.CharField(max_length=15)
    wheel_size = models.CharField(max_length=11)
    speeds = models.PositiveSmallIntegerField()
    frame = models.CharField(max_length=200)
    brakes = models.CharField(max_length=100)
    rudder = models.CharField(max_length=100)
    seat = models.CharField(max_length=100)
    footrest = models.CharField(max_length=50, blank=True)
    weight = models.FloatField()
    def __str__(self):
        return self.name


class Bike(models.Model):
    brand = models.CharField(max_length=100)
    bike_model_id = models.ForeignKey(Bike_model, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    price = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    photo = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    def __str__(self):
        return str(self.bike_model_id)


class Bike_rent(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bike_id = models.ForeignKey(Bike, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    start = models.DateTimeField()
    end = models.DateTimeField()
    region =  models.CharField(max_length=40)
    delivery_to_id = models.ForeignKey(Delivery, on_delete=models.CASCADE, blank=True, null=True)
    delivery_from_id = models.ForeignKey(Delivery, on_delete=models.CASCADE, blank=True, null=True, related_name='deliveryfrombike')
    limit = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    comment = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return str(self.bike_id)
