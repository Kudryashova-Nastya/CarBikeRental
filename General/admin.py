from django.contrib import admin

from .models import Location, User, Deliveryman, Delivery

# Register your models here.

# import and export via admin action

from import_export.admin import ImportExportActionModelAdmin

class LocationAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'city', 'metro', 'street', 'building')
    list_filter = ('city', 'metro')
    search_fields = ('id', 'city', 'metro', 'street')


class UserAdmin(ImportExportActionModelAdmin):
    list_display =('id', 'name', 'date_birth', 'gender', 'email', 'phone')
    list_filter = ('gender', 'name')
    search_fields = ('id', 'name', 'email', 'phone')


class DeliverymanAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name', 'phone', 'profile')
    list_filter = ('profile',)
    search_fields = ('id', 'name', 'phone')


class DeliveryAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'type_rent', 'deliveryman_id', 'user_id', 'location_id', 'delivery_location', 'time', 'price')
    list_filter = ('type_rent', 'time', 'price')
    search_fields = ('id',)


admin.site.register(Location, LocationAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Deliveryman, DeliverymanAdmin)
admin.site.register(Delivery, DeliveryAdmin)