# Generated by Django 2.2.5 on 2020-02-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0007_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='url',
            field=models.SlugField(blank=True, max_length=500, verbose_name='URL'),
        ),
    ]
