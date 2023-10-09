# Generated by Django 4.1.7 on 2023-10-08 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0003_remove_historicalsensormodule_air_soil_moisture_value_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalsensormodule',
            name='is_enable',
        ),
        migrations.RemoveField(
            model_name='sensormodule',
            name='is_enable',
        ),
        migrations.AddField(
            model_name='historicalsensormodule',
            name='air_soil_moisture_value',
            field=models.IntegerField(default=600),
        ),
        migrations.AddField(
            model_name='historicalsensormodule',
            name='water_soil_moisture_value',
            field=models.IntegerField(default=350),
        ),
        migrations.AddField(
            model_name='sensormodule',
            name='air_soil_moisture_value',
            field=models.IntegerField(default=600),
        ),
        migrations.AddField(
            model_name='sensormodule',
            name='water_soil_moisture_value',
            field=models.IntegerField(default=350),
        ),
    ]