from django.contrib import admin
from clinic.models import Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']
