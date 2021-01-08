from rest_framework import viewsets, permissions
from .models import Location, User, Deliveryman, Delivery
from .serializer import LocationSerializer, UserSerializer, DeliverymanSerializer, DeliverySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LocationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

class DeliverymanViewSet(viewsets.ModelViewSet):
    queryset = Deliveryman.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DeliverymanSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DeliverySerializer
    