from django.contrib import admin
from .models import Bike_model, Bike, Bike_rent

# Register your models here.

# import and export via admin action

from import_export.admin import ImportExportActionModelAdmin

def send_for_repair(modeladmin, request, queryset):
    queryset.update(status='ре')
send_for_repair.short_description = "Change the status of bikes to 'repair'"

class Bike_modelAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name', 'type_bike', 'wheel_size', 'speeds', 'frame', 'brakes', 'seat', 'rudder', 'footrest', 'weight')
    list_filter = ('type_bike', 'wheel_size', 'speeds', 'frame', 'brakes', 'seat')
    search_fields = ('id', 'name', 'weight')

class BikeAdmin(ImportExportActionModelAdmin):
    list_display =('id', 'brand', 'bike_model_id', 'price', 'year', 'location_id', 'color', 'status')
    list_filter = ('price', 'year', 'brand', 'status', 'color')
    search_fields = ('id', 'year', 'brand')
    list_editable = ('status',)
    actions = [send_for_repair, 'export_admin_action']
    def bike_model_id(self, obj):
        url = (
            reverse("admin:bike_bike_model_changelist")
            + "?"
            + urlencode({"bike_model_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">Model</a>', url)
    bike_model_id.short_description = "bike_model"

class Bike_rentAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'user_id', 'bike_id', 'status', 'start', 'end', 'region', 'delivery_to_id', 'delivery_from_id', 'limit', 'price')
    list_filter = ('status', 'start', 'end', 'region', 'limit')
    search_fields = ('id', 'start', 'end', 'region','limit', 'price', 'comment')
    list_editable = ('status',)



admin.site.register(Bike_model, Bike_modelAdmin)
admin.site.register(Bike, BikeAdmin)
admin.site.register(Bike_rent, Bike_rentAdmin)