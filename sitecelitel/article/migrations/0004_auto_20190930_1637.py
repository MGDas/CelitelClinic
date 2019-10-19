# Generated by Django 2.2.5 on 2019-09-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190930_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='caption',
            field=models.CharField(blank=True, max_length=250, verbose_name='Подпись'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='article',
            name='preview',
            field=models.TextField(blank=True, verbose_name='Превью'),
        ),
    ]