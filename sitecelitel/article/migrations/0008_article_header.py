# Generated by Django 2.2.5 on 2019-11-11 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20191111_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='header',
            field=models.BooleanField(default=True, verbose_name='Показать в шапке'),
        ),
    ]
