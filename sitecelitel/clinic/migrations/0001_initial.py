# Generated by Django 2.2.5 on 2020-01-07 21:41

import clinic.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Название')),
                ('url', models.URLField(blank=True, help_text='Пример: http://example.com/about', verbose_name='URL')),
                ('image_pc', models.ImageField(blank=True, upload_to=clinic.utils.get_image_pc, verbose_name='Изображение')),
                ('image_mob', models.ImageField(blank=True, upload_to=clinic.utils.get_image_mob, verbose_name='Изображение моб.')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдер',
                'db_table': 'sliders',
            },
        ),
    ]
