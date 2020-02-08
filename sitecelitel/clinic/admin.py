from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin

from clinic.models import Slider
from clinic.models import Partner
from clinic.models import Hospital


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'url', 'public', 'order']
    list_editable = ['public']

@admin.register(Partner)
class PartnerAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'url', 'public', 'order']
    list_editable = ['public']

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'public']
    list_editable = ['public']
