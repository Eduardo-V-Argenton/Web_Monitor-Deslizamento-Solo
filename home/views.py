from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from sensors.models import SensorsRead
from configuration.models import SensorModule
from errors.models import Errors

@login_required(redirect_field_name='login')
def info(request, sensor_module_id):
    ic = 0.0
    has_errors=False
    # Pegar os 5 últimos
    values = SensorsRead.objects.all().filter(sensor_module=sensor_module_id).order_by('timestamp').reverse()[:5]
    
    sensor_module = get_object_or_404(SensorModule, id=sensor_module_id)

    lc = sensor_module.LC
    lp = sensor_module.LP
    ll = sensor_module.LL
    last_values = []
    
    if values :
        last_values = SensorsRead.objects.filter(sensor_module=sensor_module_id).order_by('timestamp').last()
        ic = round((ll - last_values.soil_moisture) / (ll - lp),3)

    errors = Errors.objects.filter(sensor_module=sensor_module_id)

    if(errors):
        has_errors=True

    return render(request, 'home/info.html', {'values': values, 'last_values': last_values, 'id':sensor_module_id,
                                              'has_errors':has_errors, 'lc': lc, 'lp': lp, 'll': ll, 'ic':ic })

@login_required(redirect_field_name='login')
def index(request):
    sensor_modules = SensorModule.objects.all()
    return render(request, 'home/index.html', {'sensor_modules':sensor_modules}) 

@login_required(redirect_field_name='login')
def calibrate(request, sensor_module_id):
    sensor_module = get_object_or_404(SensorModule, id=sensor_module_id)

    if request.method == 'POST':
        print(request.POST.get('air_value'))
        sensor_module.air_soil_moisture_value = request.POST.get('air_value')
        sensor_module.water_soil_moisture_value = request.POST.get('water_value')
        sensor_module.save()
        return redirect(info, sensor_module_id)
    return render(request, 'home/calibrate.html', {
        'air_value': sensor_module.air_soil_moisture_value, 
        'water_value': sensor_module.water_soil_moisture_value,
        'id':sensor_module_id
    })
