from django.contrib import admin
from vacancy.models import Vacancy, Group
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Vacancy)
class Vacancy(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = [
        'position',
        'group',
        'city',
        'phone',
        'email',
        'created',
        'updated'
    ]

admin.site.register(Group)
