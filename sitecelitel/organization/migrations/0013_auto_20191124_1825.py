# Generated by Django 2.2.5 on 2019-11-24 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0012_auto_20191124_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='price_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agreement', to='service.PriceType', verbose_name='Тип цены'),
        ),
    ]