from rest_framework import serializers
from .models import Car_model, Car, Car_rent

class Car_modelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_model
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class Car_rentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_rent
        fields = '__all__'