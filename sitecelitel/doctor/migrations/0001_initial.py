# Generated by Django 2.2.5 on 2019-09-28 15:32

from django.db import migrations, models
import django.db.models.deletion
import doctor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Публикация')),
                ('code', models.CharField(max_length=11)),
                ('main_code', models.CharField(blank=True, max_length=11)),
                ('full_name', models.CharField(max_length=255, verbose_name='Полное имя')),
                ('photo', models.ImageField(blank=True, upload_to=doctor.models.create_name, verbose_name='Фото')),
                ('avatar', models.ImageField(blank=True, upload_to=doctor.models.create_name, verbose_name='Аватарка')),
                ('experience', models.CharField(blank=True, max_length=45, verbose_name='Опыт')),
                ('academic_degree', models.CharField(blank=True, max_length=100, verbose_name='Ученая степень')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('special_note', models.TextField(blank=True, null=True, verbose_name='Примечание')),
                ('department', models.ManyToManyField(blank=True, related_name='department', to='organization.Department', verbose_name='Депортамент')),
            ],
            options={
                'verbose_name': 'Доктор',
                'verbose_name_plural': 'Доктора',
                'db_table': 'doctors',
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=36)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Специялизация',
                'verbose_name_plural': 'Специализации',
                'db_table': 'specialization',
            },
        ),
        migrations.CreateModel(
            name='DoctorTiming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField(verbose_name='Начало')),
                ('time_end', models.TimeField(verbose_name='Конец')),
                ('date', models.DateField(verbose_name='Дата')),
                ('active', models.BooleanField(default=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timing', to='doctor.Doctor', verbose_name='Доктор')),
            ],
            options={
                'verbose_name': 'Приём',
                'verbose_name_plural': 'Приёмы',
                'db_table': 'doctor_timing',
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='doctor', to='doctor.Specialization', verbose_name='Специализация'),
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=45, verbose_name='Название')),
                ('question', models.TextField(blank=True, verbose_name='Вопрос')),
                ('answer', models.TextField(blank=True, verbose_name='Ответ')),
                ('done', models.BooleanField(default=False, verbose_name='Статус')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('date_quest', models.DateTimeField(auto_now_add=True, verbose_name='Дата вопроса')),
                ('date_answer', models.DateTimeField(auto_now=True, verbose_name='Дата ответа')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultation', to='doctor.Doctor', verbose_name='Доктор')),
            ],
            options={
                'verbose_name': 'Консультация',
                'verbose_name_plural': 'Консультации',
                'db_table': 'consultation',
            },
        ),
    ]