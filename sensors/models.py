from django.db import models

class SensorsRead(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)   
    danger_level=models.IntegerField(default=0, blank=False, null=False)   
    accel_x=models.FloatField()   
    accel_y=models.FloatField()   
    accel_z=models.FloatField()   
    air_temperature=models.FloatField(blank=True, null=True)   
    air_humidity=models.FloatField(blank=True, null=True)   
    soil_moisture=models.IntegerField()   
    rain_sensor_value=models.IntegerField()   