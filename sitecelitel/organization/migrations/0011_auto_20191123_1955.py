# Generated by Django 2.2.5 on 2019-11-23 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0010_auto_20191123_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='instagram_tag',
            field=models.CharField(blank=True, max_length=50, verbose_name='Инстаграм тег'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='instagram',
            field=models.URLField(blank=True, max_length=45, verbose_name='Инстаграм URL'),
        ),
    ]
