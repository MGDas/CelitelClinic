from django.contrib import admin
from tag.models import ArticleTag, DoctorTag

admin.site.register(ArticleTag)
admin.site.register(DoctorTag)
