from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from new.models import New

@admin.register(New)
class NewAdmin(SummernoteModelAdmin):
    summernote_fields = ['preview', 'content']
    list_display = ['title', 'header', 'public', 'created', 'updated']
    list_editable = ['public']

    filter_horizontal = ['doctors']
