from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from doctor.models import (
    Doctor, Specialization, DoctorTiming, Consultation, Review, Video, Timing
    )

@admin.register(Doctor)
class DoctorAdmin(SummernoteModelAdmin):
    summernote_fields = ['content', 'special_note']
    list_display = ['full_name', 'code']
    search_fields = ['full_name']
    
@admin.register(Video)
class VideoAdmin(SummernoteModelAdmin):
    summernote_fields = ['video']
    list_display = ['title', 'created', 'updated', 'public']
    list_editable = ['public']

    filter_horizontal = ['doctor']

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']

@admin.register(Timing)
class TimingAdmin(admin.ModelAdmin):
    list_display = ['date', 'start', 'end']

admin.site.register(DoctorTiming)
admin.site.register(Consultation)
admin.site.register(Review)
