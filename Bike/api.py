from rest_framework import viewsets, permissions
from .models import Bike_model, Bike, Bike_rent
from .serializer import Bike_modelSerializer, BikeSerializer, Bike_rentSerializer

class Bike_modelViewSet(viewsets.ModelViewSet):
    queryset = Bike_model.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Bike_modelSerializer

class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BikeSerializer

class Bike_rentViewSet(viewsets.ModelViewSet):
    queryset = Bike_rent.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Bike_rentSerializer
    