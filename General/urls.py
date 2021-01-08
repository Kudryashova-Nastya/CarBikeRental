from rest_framework import routers
from .api import LocationViewSet, UserViewSet, DeliverymanViewSet, DeliveryViewSet
from Car.api import Car_modelViewSet, CarViewSet, Car_rentViewSet
from Bike.api import Bike_modelViewSet, BikeViewSet, Bike_rentViewSet

router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')
router.register('api/locations', LocationViewSet, 'locations')
router.register('api/deliverymans', DeliverymanViewSet, 'deliverymans')
router.register('api/deliverys', DeliveryViewSet, 'deliverys')
router.register('api/car_models', Car_modelViewSet, 'car_models')
router.register('api/cars', CarViewSet, 'cars')
router.register('api/car_rents', Car_rentViewSet, 'car_rents')
router.register('api/bike_models', Bike_modelViewSet, 'bike_models')
router.register('api/bikes', BikeViewSet, 'bikes')
router.register('api/bike_rents', Bike_rentViewSet, 'bike_rents')
urlpatterns = router.urls