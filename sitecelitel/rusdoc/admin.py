from django.contrib import admin
from rusdoc.models import RussianDoctor
from django_summernote.admin import SummernoteModelAdmin


@admin.register(RussianDoctor)
class RussionDoctorAdmin(SummernoteModelAdmin):
    summernote_fields = ['preview', 'content']
    fields = [
        ('public', 'header'),
        'title',
        'note',
        'preview',
        'content',
        'image',
        'capcha',
        'data_start',
        'data_end'
    ]
    list_display = ['title', 'note', 'data_start', 'data_end', 'public',]
