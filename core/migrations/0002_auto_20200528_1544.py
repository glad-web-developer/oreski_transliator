# Generated by Django 3.0.6 on 2020-05-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nabormedia',
            name='skorost_perelistivanie_slaida',
            field=models.PositiveIntegerField(default=7, verbose_name='Скорость перелистывание слайда в секундах'),
        ),
    ]
