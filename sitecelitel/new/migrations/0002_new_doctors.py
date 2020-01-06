# Generated by Django 2.2.5 on 2020-01-03 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='doctors',
            field=models.ManyToManyField(blank=True, related_name='news', to='doctor.Doctor', verbose_name='Доктора'),
        ),
    ]