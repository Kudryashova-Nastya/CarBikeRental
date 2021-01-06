from django.db import models

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=100)
    metro = models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=10)
    def __str__(self):
        return self.street


class User(models.Model):
    name = models.CharField(max_length=100)
    date_birth = models.DateField()
    gender = models.CharField(max_length=1, blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    photo = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name

class Deliveryman(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    profile = models.CharField(max_length=10)
    photo = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Delivery(models.Model):
    type_rent = models.CharField(max_length=8)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    deliveryman_id = models.ForeignKey(Deliveryman, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    delivery_location = models.CharField(max_length=100)
    time = models.DateTimeField()
    price = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.delivery_location