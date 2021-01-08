from rest_framework import serializers
from .models import Bike_model, Bike, Bike_rent

class Bike_modelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike_model
        fields = '__all__'

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'

class Bike_rentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike_rent
        fields = '__all__'