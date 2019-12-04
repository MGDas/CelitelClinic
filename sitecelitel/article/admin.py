from django.contrib import admin
from article.models import Article, Rating, About
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Rating)

@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    fields = [
        ('public', 'header'),
        'doctor',
        'title',
        'slug',
        'preview',
        'content',
        ('image', 'caption'),
        'created',
        'updated',
        'tags'
    ]

    summernote_fields = ('preview', 'content',)
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'doctor', 'slug', 'id', 'public', 'created', 'updated']
    list_editable = ['public']
    list_filter = ['public']

    filter_horizontal = ['tags']

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ['title', 'created', 'updated']
    fields = [
        ('created', 'updated'),
        'title',
        'content',
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
         return False
