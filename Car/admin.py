from django.contrib import admin

from .models import Car_model, Car, Car_rent

from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe 

# Register your models here.

# import and export via admin action

from import_export.admin import ImportExportActionModelAdmin

def send_for_repair(modeladmin, request, queryset):
    queryset.update(status='ре')
send_for_repair.short_description = "Change the status of cars to 'repair'"

class Car_modelAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name', 'gearbox', 'body', 'seats', 'drive', 'engine', 'doors', 'rudder')
    list_filter = ('gearbox', 'body', 'engine', 'seats', 'drive', 'doors', 'rudder')
    search_fields = ('id', 'name')
    # from_encoding = 'cp1251'
    # to_encoding = 'cp1251'

class CarAdmin(ImportExportActionModelAdmin):
    list_display =('id', 'brand', 'car_model_id', 'price', 'year', 'location_id', 'max_limit', 'mileage', 'color', 'number', 'status')
    list_filter = ('price', 'year', 'max_limit', 'brand', 'status', 'color')
    search_fields = ('id', 'number', 'year', 'brand')
    list_editable = ('status',)
    actions = [send_for_repair, 'export_admin_action']
   
    def car_model_id(self, obj):
        url = (
            reverse("admin:car_car_model_changelist")
            # + "?"
            # + urlencode({"car_model__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">Students</a>', url)
    car_model_id.short_description = "car_model"
    
    # def car_model_id(self, item):
        #     url = resolve_url(admin_urlname(models.Car._meta, 'change'), item.bar.id)
        #     return format_html('<a href="{url}">{name}</a>'.format(url=url, name=str(item.bar)))
        
        # return mark_safe('<a href="{}">{}</a>'.format(
        #     reverse("admin:auth_car_model_change", args=(obj.car_model.id,)),
        #     obj.car_model.name
        # ))
    #     c = Car_model.objects.get(id = obj.id)
    #     url = (
    #         reverse("admin:car_car_model_change", args=(c.id,))
    #     )
    #     return format_html('<a href="{}"> {obj.id}</a>', url)
    # car_model_id.short_description = "car_model"

    # def car_model_id(self, item):
    #     from django.shortcuts import resolve_url
    #     from django.contrib.admin.templatetags.admin_urls import admin_urlname
    #     url = resolve_url(admin_urlname(models.Bar._meta, 'change'), item.bar.id)
    #     return format_html('<a href="{url}">{name}</a>'.format(url=url, name=str(item.bar)))

class Car_rentAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'user_id', 'car_id', 'status', 'start', 'end', 'region', 'delivery_to_id', 'delivery_from_id', 'limit', 'price')
    list_filter = ('status', 'start', 'end', 'region', 'limit')
    search_fields = ('id', 'start', 'end', 'region','limit', 'price', 'comment')
    list_editable = ('status',)



admin.site.register(Car_model, Car_modelAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Car_rent, Car_rentAdmin)