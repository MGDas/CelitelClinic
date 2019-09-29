from django.contrib import admin
from doctor.models import (
    Doctor, Specialization, DoctorTiming, Consultation, Review, Video
    )

admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(DoctorTiming)
admin.site.register(Consultation)
admin.site.register(Review)
admin.site.register(Video)
