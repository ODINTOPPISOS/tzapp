# Generated by Django 4.0.5 on 2022-06-22 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_title', models.CharField(max_length=50, verbose_name='Название объекта')),
                ('object_imgur', models.CharField(max_length=200, verbose_name='Изображение объекта')),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_count', models.FloatField(max_length=1000, verbose_name='Количество объектов')),
                ('object_price', models.FloatField(max_length=1000, verbose_name='Цена объекта')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poebota.object')),
            ],
        ),
    ]