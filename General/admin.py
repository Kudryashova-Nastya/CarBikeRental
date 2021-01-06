from django.contrib import admin

from .models import Location, User, Deliveryman, Delivery

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'metro', 'street', 'building')
    list_filter = ('city', 'metro')
    search_fields = ('id', 'city', 'metro', 'street')

class UserAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'date_birth', 'gender', 'email', 'phone')
    list_filter = ('gender', 'name')
    search_fields = ('id', 'name', 'email', 'phone')


class DeliverymanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'profile')
    list_filter = ('profile',)
    search_fields = ('id', 'name', 'phone')



class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_rent', 'deliveryman_id', 'user_id', 'location_id', 'delivery_location', 'time', 'price')
    list_filter = ('type_rent', 'time', 'price')
    search_fields = ('id',)



admin.site.register(Location, LocationAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Deliveryman, DeliverymanAdmin)
admin.site.register(Delivery, DeliveryAdmin)