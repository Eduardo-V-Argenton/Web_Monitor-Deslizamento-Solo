# Generated by Django 4.1.7 on 2023-10-22 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorsRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('danger_level', models.IntegerField(default=0)),
                ('accel_x', models.FloatField()),
                ('accel_y', models.FloatField()),
                ('accel_z', models.FloatField()),
                ('air_temperature', models.FloatField(blank=True, null=True)),
                ('air_humidity', models.FloatField(blank=True, null=True)),
                ('soil_moisture', models.IntegerField()),
                ('rain_sensor_value', models.IntegerField()),
                ('sensor_module', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='configuration.sensormodule')),
            ],
        ),
    ]
