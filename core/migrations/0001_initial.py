# Generated by Django 3.0.6 on 2020-05-28 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NaborMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazvanie', models.CharField(max_length=250, verbose_name='Название')),
                ('recomendovania_prodolzitelnost', models.CharField(blank=True, max_length=250, null=True, verbose_name='Рекомендованная продолжительность набора')),
                ('skorost_perelistivanie_slaida', models.IntegerField(verbose_name='Скорость перелистывание слайда в секундах')),
            ],
            options={
                'verbose_name': 'Набор медиа',
                'verbose_name_plural': 'Набор медиа',
            },
        ),
        migrations.CreateModel(
            name='SpisokVosproizvedenia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Дата')),
                ('vremia_s', models.TimeField(verbose_name='Время показа с ')),
                ('vremia_po', models.TimeField(verbose_name='Время показа по ')),
                ('zvuk', models.BooleanField(default=True, verbose_name='Звук')),
                ('local_id_hash', models.CharField(blank=True, max_length=250, null=True)),
                ('nabor_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.NaborMedia', verbose_name='Набор медиа')),
            ],
            options={
                'verbose_name': 'Список воспроизведения',
                'verbose_name_plural': 'Список воспроизведения',
            },
        ),
        migrations.CreateModel(
            name='RaspisaniePoDniam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('den_nedeli', models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')], verbose_name='День недели')),
                ('vremia_s', models.TimeField(verbose_name='Время показа с ')),
                ('vremia_po', models.TimeField(verbose_name='Время показа по ')),
                ('zvuk', models.BooleanField(default=True, verbose_name='Звук')),
                ('nabor_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.NaborMedia', verbose_name='Набор медиа')),
            ],
            options={
                'verbose_name': 'Расписание по дням',
                'verbose_name_plural': 'Список воспроизведения',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_media', models.CharField(choices=[('Видео', 'Видео'), ('Аудио', 'Аудио'), ('Фото', 'Фото')], max_length=255, verbose_name='Тип медиа')),
                ('media', models.FileField(upload_to='', verbose_name='Файл')),
                ('nabor_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rn_media', to='core.NaborMedia', verbose_name='Набор медиа')),
            ],
            options={
                'verbose_name': 'Медиа',
                'verbose_name_plural': 'Медиа',
            },
        ),
    ]
