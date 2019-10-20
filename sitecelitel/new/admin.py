from django.contrib import admin
from new.models import New

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['title', 'header', 'public', 'created', 'updated']

    filter_horizontal = ['doctors']
