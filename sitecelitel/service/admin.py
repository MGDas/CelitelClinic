from django.contrib import admin
from service.models import (
    ServiceGroup, Service, PriceType, Price
)

admin.site.register(ServiceGroup)
admin.site.register(Service)
admin.site.register(PriceType)
admin.site.register(Price)
