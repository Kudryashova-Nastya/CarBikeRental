from django.db import models

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=100)
    metro = models.CharField(max_length=30)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=10)


class User(models.Model):
    name = models.CharField(max_length=100)
    date_birth = models.DateField()
    gender = models.CharField(max_length=1, blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    photo = models.CharField(max_length=100, blank=True)


class Deliveryman(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    profile = models.CharField(max_length=10)
    photo = models.CharField(max_length=100)


class Delivery(models.Model):
    type_rent = models.CharField(max_length=8)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    deliveryman_id = models.ForeignKey(Deliveryman, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    delivery_location = models.CharField(max_length=100)
    time = models.DateTimeField()
    price = models.PositiveSmallIntegerField()

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
