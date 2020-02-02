# Generated by Django 2.2.5 on 2020-02-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='doctors', to='tag.DoctorTag', verbose_name='Теги'),
        ),
    ]
