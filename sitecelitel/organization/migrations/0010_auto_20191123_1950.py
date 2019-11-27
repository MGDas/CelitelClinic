# Generated by Django 2.2.5 on 2019-11-23 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0008_organization_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='organization',
            name='public',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AddField(
            model_name='organization',
            name='updated',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='operating_mode',
            field=models.TextField(blank=True, verbose_name='График работы'),
        ),
    ]