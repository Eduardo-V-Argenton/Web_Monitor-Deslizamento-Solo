# Generated by Django 4.1.7 on 2023-09-10 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorsread',
            name='air_humidity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensorsread',
            name='air_temperature',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
