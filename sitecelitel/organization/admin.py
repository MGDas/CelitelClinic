from django.contrib import admin
from organization.models import (
    Organization, Department, Agreement
)


admin.site.register(Organization)
admin.site.register(Department)
admin.site.register(Agreement)
