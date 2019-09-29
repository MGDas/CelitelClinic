from django.db import models

# Create your models here.
class TagDoctor(models.Model):
    tags = models.ManyToMany(
        Doctor,
        on_delete=models.DO_NOTHING,
        related_name='tagdoctor',
        null=True,
        blank=True,
        verbose_name='Доктор(а)'
    )

    tags_type = models.ForeignKey(
        'TagsType',
        on_delete=models.DO_NOTHING,
        related_name='tagdoctor',
        null=True,
        blank=True,
        verbose_name='Тип тега'
    )

    tag = models.CharField(max_length=255, verbose_name='Заголовок')

    class Meta:
        db_table = 'tags_doctors'



class TagsType(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags_type'


class TagsArticle(BaseModel):
    tags = models.ManyToMany(Article, on_delete=models.DO_NOTHING, blank=True, verbose_name='Статьи')
    tags_type = models.ForeignKey('TagsType', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Тип тега')
    tag_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Тег')

    class Meta:
        db_table = 'tags_article'
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'

    def __str__(self):
        return self.tag_name
