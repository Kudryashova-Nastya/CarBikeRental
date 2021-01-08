from rest_framework import viewsets, permissions
from .models import Car_model, Car, Car_rent
from .serializer import Car_modelSerializer, CarSerializer, Car_rentSerializer

class Car_modelViewSet(viewsets.ModelViewSet):
    queryset = Car_model.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Car_modelSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

class Car_rentViewSet(viewsets.ModelViewSet):
    queryset = Car_rent.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Car_rentSerializer
    