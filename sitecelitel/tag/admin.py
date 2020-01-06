from django.contrib import admin
from tag.models import ArticleTag, DoctorTag

@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug', 'header', 'public']
    list_editable = ['header', 'public']

@admin.register(DoctorTag)
class DoctorTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug', 'header', 'public']
    list_editable = ['header', 'public']
