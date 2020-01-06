# Generated by Django 2.2.5 on 2020-01-03 15:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Публикация')),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated', models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления')),
                ('question', models.TextField(blank=True, verbose_name='Вопрос')),
                ('answer', models.TextField(blank=True, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Faq',
                'verbose_name_plural': 'Faqs',
                'db_table': 'faq',
            },
        ),
    ]
