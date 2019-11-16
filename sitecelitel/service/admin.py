from django.contrib import admin
from service.models import (
    ServiceGroup, Service, PriceType, Price
)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(ServiceGroup)
admin.site.register(PriceType)
admin.site.register(Price)
