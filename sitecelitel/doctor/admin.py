from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from doctor.models import Doctor
from doctor.models import Specialization
from doctor.models import DoctorTiming
from doctor.models import Consultation
from doctor.models import Review
from doctor.models import Video
from doctor.models import Timing


@admin.register(Doctor)
class DoctorAdmin(SummernoteModelAdmin):
    summernote_fields = ['content', 'special_note']
    list_display = ['full_name', 'code']
    search_fields = ['full_name']

    fields = (
        ('id', 'code', 'main_code',),
        ("full_name", "the_best",),
        "gender",
        ("childish", "adult",),
        "photo", "avatar",
        ("experience", "academic_degree",),
        ("specialization", "department",), "tags",
        "content", "special_note"
    )
    readonly_fields = ('id', 'code', 'main_code')

    filter_horizontal = ['tags']

    
@admin.register(Video)
class VideoAdmin(SummernoteModelAdmin):
    summernote_fields = ['video']
    list_display = ['title', 'created', 'public']
    list_editable = ['public']
    
    filter_horizontal = ['doctor']


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    search_fields = ['name', 'code']


@admin.register(Timing)
class TimingAdmin(admin.ModelAdmin):
    list_display = ['date', 'start', 'end']


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['question', 'email', 'doctor', 'date_quest', 'id']
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review', 'author', 'doctor', 'created', 'id']


admin.site.register(DoctorTiming)
