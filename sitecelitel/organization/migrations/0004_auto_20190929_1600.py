# Generated by Django 2.2.5 on 2019-09-29 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20190929_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='organization',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='organization.Organization', verbose_name='Организация'),
        ),
    ]
