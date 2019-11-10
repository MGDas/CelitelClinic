# Generated by Django 2.2.5 on 2019-11-10 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20191021_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='doctor.Doctor', verbose_name='Доктор'),
        ),
    ]
