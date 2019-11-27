# Generated by Django 2.2.5 on 2019-11-24 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0012_auto_20191124_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('m', 'Мужчина'), ('w', 'Женщина'), ('n', 'Нет пола')], default='n', max_length=1, verbose_name='Пол'),
        ),
    ]
