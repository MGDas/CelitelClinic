# Generated by Django 2.2.5 on 2019-11-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_merge_20191122_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='Город'),
        ),
    ]