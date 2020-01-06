# from django.contrib import admin
# from service.models import (
#     ServiceGroup, Service, PriceType, Price
# )
#
# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     search_fields = ['name', 'service_group__name']
#     list_display = ['name', 'service_group']
#
#     filter_horizontal = ['doctors']
#
# @admin.register(Price)
# class PriceAdmin(admin.ModelAdmin):
#     list_display = ['service', 'price_type', 'price']
#     search_fields = ['service']
#
# admin.site.register(ServiceGroup)
# admin.site.register(PriceType)
