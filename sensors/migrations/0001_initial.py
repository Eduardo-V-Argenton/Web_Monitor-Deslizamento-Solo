# Generated by Django 4.1.7 on 2023-09-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('air_temperature', models.FloatField()),
                ('air_humidity', models.FloatField()),
                ('soil_moisture', models.IntegerField()),
                ('rain_sensor_value', models.IntegerField()),
            ],
        ),
    ]
