# Generated by Django 4.1.7 on 2023-10-22 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalsensormodule',
            old_name='accel_last_x',
            new_name='accel_default_x',
        ),
        migrations.RenameField(
            model_name='historicalsensormodule',
            old_name='accel_last_y',
            new_name='accel_default_y',
        ),
        migrations.RenameField(
            model_name='historicalsensormodule',
            old_name='accel_last_z',
            new_name='accel_default_z',
        ),
        migrations.RenameField(
            model_name='sensormodule',
            old_name='accel_last_x',
            new_name='accel_default_x',
        ),
        migrations.RenameField(
            model_name='sensormodule',
            old_name='accel_last_y',
            new_name='accel_default_y',
        ),
        migrations.RenameField(
            model_name='sensormodule',
            old_name='accel_last_z',
            new_name='accel_default_z',
        ),
    ]
