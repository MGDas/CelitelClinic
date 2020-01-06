from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from faq.models import Faq

@admin.register(Faq)
class FaqAdmin(SummernoteModelAdmin):
    summernote_fields = ('answer',)
    list_display = ['__str__', 'created', 'updated', 'public']
