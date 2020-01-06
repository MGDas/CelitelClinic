from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from organization.models import (
    Organization, Department, Agreement
)

@admin.register(Organization)
class OrganizationAdmin(SummernoteModelAdmin):
    summernote_fields = ['panorama', 'map', 'operating_mode']
    list_display = [
        'name',
        'namefull',
        'city',
        'address',
        'operating_mode',
        'site',
        'instagram',
        'phone_registry',
        'phone_callcenter',
        'created',
        'updated',
        'public'
    ]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'codeparent',
        'organization', 'public', 'created', 'updated']

admin.site.register(Agreement)
