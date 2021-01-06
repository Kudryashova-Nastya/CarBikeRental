from django.contrib import admin
from .models import Bike_model, Bike, Bike_rent

# Register your models here.

class Bike_modelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type_bike', 'wheel_size', 'speeds', 'frame', 'brakes', 'seat', 'rudder', 'footrest', 'weight')
    list_filter = ('type_bike', 'wheel_size', 'speeds', 'frame', 'brakes', 'seat')
    search_fields = ('id', 'name', 'weight')

class BikeAdmin(admin.ModelAdmin):
    list_display =('id', 'brand', 'bike_model_id', 'price', 'year', 'location_id', 'color', 'status')
    list_filter = ('price', 'year', 'brand', 'status', 'color')
    search_fields = ('id', 'year', 'brand')
    list_editable = ('status',)

class Bike_rentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'bike_id', 'status', 'start', 'end', 'region', 'delivery_to_id', 'delivery_from_id', 'limit', 'price')
    list_filter = ('status', 'start', 'end', 'region', 'limit')
    search_fields = ('id', 'start', 'end', 'region','limit', 'price', 'comment')
    list_editable = ('status',)



admin.site.register(Bike_model, Bike_modelAdmin)
admin.site.register(Bike, BikeAdmin)
admin.site.register(Bike_rent, Bike_rentAdmin)