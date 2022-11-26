from os import O_WRONLY
from django.shortcuts import render
from .models import Driver, Vehicle

def DriverFunc(request):
    id = 1
    allVehicles = Vehicle.objects.filter(owner=id)
    allVehiclesDict = {
        'allVehicles': allVehicles
    }
    return render(request, 'driver.html', allVehiclesDict)

def BookRide(request):
    allVehicles = Vehicle.objects.all()
    allVehiclesDict = {
        'allVehicles': allVehicles
    }
    return render(request, 'customer.html', allVehiclesDict)

def AddVehicle(request):
    print("data is", request.POST)
    id = request.POST['id']
    type = request.POST['vehicleType']
    time = request.POST['vehicleTime']
    price = request.POST['vehiclePrice']
    name = request.POST['name']
    allVehicles = Vehicle.objects.filter(id=id)
    allVehiclesDict = {
        'allVehicles': allVehicles
    }
    driverIns = Driver.objects.get(id=id)
    Vehicle.objects.create(owner=driverIns, name=name, type=type, price=price, time=time)


    return render(request, 'driver.html',allVehiclesDict)