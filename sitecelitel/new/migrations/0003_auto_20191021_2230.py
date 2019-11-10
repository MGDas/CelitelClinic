# Generated by Django 2.2.5 on 2019-10-21 19:30

from django.db import migrations, models
import sitecelitel.utils


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_auto_20191020_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='caption',
            field=models.CharField(blank=True, max_length=255, verbose_name='Подпись'),
        ),
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(blank=True, upload_to=sitecelitel.utils.get_photo, verbose_name='Изображение'),
        ),
    ]
