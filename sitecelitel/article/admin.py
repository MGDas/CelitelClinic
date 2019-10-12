from django.contrib import admin
from article.models import Article, Rating
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Rating)

@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('preview', 'content',)
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'doctor', 'slug', 'id']
