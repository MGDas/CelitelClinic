# Generated by Django 2.2.5 on 2020-01-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('promotion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='doctor',
            field=models.ManyToManyField(blank=True, related_name='promotions', to='doctor.Doctor', verbose_name='Доктор'),
        ),
    ]
