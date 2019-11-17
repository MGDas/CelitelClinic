from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from doctor.models import (
    Doctor, Specialization, DoctorTiming, Consultation, Review, Video, Timing
    )

@admin.register(Doctor)
class DoctorAdmin(SummernoteModelAdmin):
    summernote_fields = ['content', 'special_note']

@admin.register(Video)
class VideoAdmin(SummernoteModelAdmin):
    summernote_fields = ['video']
    list_display = ['title', 'created', 'updated', 'public']
    list_editable = ['public']

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Timing)
class TimingAdmin(admin.ModelAdmin):
    list_display = ['date', 'hour']

admin.site.register(DoctorTiming)
admin.site.register(Consultation)
admin.site.register(Review)
