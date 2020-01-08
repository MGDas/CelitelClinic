from django.contrib import admin
from clinic.models import Slider
from adminsortable2.admin import SortableAdminMixin


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'url', 'public', 'order']
    list_editable = ['public']
