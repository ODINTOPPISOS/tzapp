# Generated by Django 4.0.5 on 2022-07-01 07:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('poebota', '0004_alter_bron_bron_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bron',
            name='bron_login',
            field=models.CharField(default='', max_length=50, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='bron',
            name='bron_password',
            field=models.CharField(default='', max_length=50, verbose_name='Пароль для бронирования'),
        ),
        migrations.AlterField(
            model_name='bron',
            name='bron_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 1, 7, 5, 10, 421494, tzinfo=utc)),
        ),
    ]
