# Generated by Django 2.2.5 on 2020-01-03 15:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import sitecelitel.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Публикация')),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated', models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
                'db_table': 'about',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Публикация')),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated', models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Уникальное имя')),
                ('preview', models.TextField(blank=True, verbose_name='Превью')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('caption', models.CharField(blank=True, max_length=250, verbose_name='Подпись')),
                ('image', models.ImageField(blank=True, upload_to=sitecelitel.utils.get_photo, verbose_name='Изображение')),
                ('header', models.BooleanField(default=True, verbose_name='Показать в шапке')),
                ('tags', models.ManyToManyField(blank=True, related_name='articles', to='tag.ArticleTag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'db_table': 'article',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.PositiveIntegerField(default=0)),
                ('dislike', models.PositiveIntegerField(default=0)),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='article.Article')),
            ],
            options={
                'db_table': 'rating',
            },
        ),
    ]
