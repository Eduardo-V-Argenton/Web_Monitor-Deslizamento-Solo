from django.db import models
from django import forms
import re

class Module(models.Model):
    addh=models.IntegerField(default=0, blank=False, null=False)
    addl=models.IntegerField(default=0, blank=False, null=False)
    transmission_power=models.CharField(max_length=1, default='0', blank=False, null=False)
    enable_lbt=models.BooleanField(default=False, blank=False, null=False)
    
    fields_command = []
    
    def print_module(self):
        values = []
        for field in self.fields_command:
            if re.match(r'^enable_', field):
                values.append(str(int(getattr(self, field))))
            else:
                values.append(str(getattr(self, field)))
        return ";".join(values)
    

    
class ControlModule(Module):
    read_command_period= models.IntegerField(default=3, blank=False, null=False)

    fields_command = [
        'addh','addl','transmission_power','enable_lbt','read_command_period'
    ]
class SensorModule(Module):
    is_enable=models.BooleanField(default=False, null=False)
    name=models.CharField(max_length=255, blank=False, null=False, unique=True)
    #LoRa
    channel=models.IntegerField(default=64, blank=False, null=False)
    wor_period=models.CharField(max_length=1, default='3', blank=False, null=False)
    air_data_rate=models.CharField(max_length=1, default='2', blank=False, null=False)
    crypth=models.IntegerField(default=0, blank=False, null=False)
    cryptl=models.IntegerField(default=0, blank=False, null=False)
    #System
    timeout_sensors_read_packet = models.FloatField(default=60, blank=False, null=False)
    timeout_config_packet = models.FloatField(default=60, blank=False, null=False)
    timeout_handshake = models.FloatField(default=60, blank=False, null=False)
    timeout_SYN = models.FloatField(default=20, blank=False, null=False)
    timeout_SYNACK = models.FloatField(default=20, blank=False, null=False)
    timeout_ACK = models.FloatField(default=20, blank=False, null=False)
    auto_send_sensors_period= models.FloatField(default=10, blank=False, null=False)

    fields_command = [
        'id','addh','addl','transmission_power','enable_lbt', 'channel', 
        'wor_period', 'air_data_rate', 'crypth', 'cryptl','timeout_sensors_read_packet',
        'timeout_config_packet','timeout_sensors_read_packet','timeout_handshake','timeout_SYN','timeout_SYNACK',
        'timeout_ACK'
    ]
    
class ModuleObserver(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)   
    is_controller=models.BooleanField(default=False, blank=False,null=False)
    module=models.ForeignKey(to=Module, related_name="fk_module", on_delete=models.SET("ERASED"))
    executed=models.BooleanField(default=False)


    def calculate_crc16(self,data):
        crc = 0xFFFF
        polynomial = 0x1021

        for char in data:
            byte = ord(char)  
            crc ^= (byte << 8)
            for _ in range(8):
                if crc & 0x8000:
                    crc = (crc << 1) ^ polynomial
                else:
                    crc <<= 1
                crc &= 0xFFFF
        
        return crc

    def print_command(self, read_sensors=False):
        if(self.executed == 0):
            if(self.is_controller):
                module = ControlModule.objects.get(id=self.module.id)
            else:
                module = SensorModule.objects.get(id=self.module.id)
            module = module.print_module()
            message = ('2 ' if read_sensors else (str(int(self.is_controller))))+';'+module
            crc = self.calculate_crc16(message)
            return message+';'+str(int(crc))
        return ''

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields='__all__'

        
    AIR_DATA_RATE_CHOICES = [
        ('2', '2.4k'),
        ('3', '4.8k'),
        ('4', '9.6k'),
        ('5', '19.2k'),
        ('6', '38.4k'),
        ('7', '62.5k'),
    ]
    
    TRANSMISSION_POWER_CHOICES = [
        ('0', '22'),
        ('1', '17'),
        ('2', '13'),
        ('3', '10'),
    ]

    WOR_PERIOD_CHOICES = [
        ('0','500'),
        ('1','1000'),
        ('2','500'),
        ('3','2000'),
        ('4','2500'),
        ('5','3000'),
        ('6','3500'),
        ('7','4000'),
    ]
    
    air_data_rate = forms.ChoiceField(choices=AIR_DATA_RATE_CHOICES)
    transmission_power = forms.ChoiceField(choices=TRANSMISSION_POWER_CHOICES)
    wor_period = forms.ChoiceField(choices=WOR_PERIOD_CHOICES)


class SensorModuleForm(ModuleForm):
    class Meta:
        model = SensorModule
        exclude= 'is_enable', 


class ControlModuleForm(ModuleForm):
    class Meta:
        model = ControlModule
        fields='__all__'
