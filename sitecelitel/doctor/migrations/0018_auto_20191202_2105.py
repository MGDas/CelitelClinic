# Generated by Django 2.2.5 on 2019-12-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0017_merge_20191202_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timing',
            name='end',
            field=models.CharField(blank=True, max_length=5, verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='timing',
            name='start',
            field=models.CharField(blank=True, max_length=5, verbose_name='Начало'),
        ),
    ]
