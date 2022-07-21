# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Car, Tires
from .forms import FuelingForm
# Add the following import
from django.http import HttpResponse

# # Add the Cat class & list and view function below the imports
# class Car:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, manufacturer, horsepower):
#     self.name = name
#     self.manufacturer = manufacturer
#     self.horsepower = horsepower
   

# cars = [
#   Car('Supra', 'Toyota', 600),
#   Car('M3', 'BMW', 580),
#   Car('WRX STI', 'Subaru', 310)
# ]

# Define the home view
def home(request):
  return HttpResponse('<h1>This is the app home page</h1>')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    id_list = car.tires.all().values_list('id')
    tires_car_doesnt_have = Tires.objects.exclude(id__in=id_list)
    fueling_form = FuelingForm()
    return render(request, 'cars/detail.html', {'car': car, 'fueling_form': fueling_form, 'tires': tires_car_doesnt_have})

def add_fueling(request, car_id):

  form = FuelingForm(request.POST)
  
  if form.is_valid():
    new_fueling = form.save(commit=False)
    new_fueling.car_id = car_id
    new_fueling.save()
  return redirect('detail', car_id=car_id)

class CarCreate(CreateView):
  model = Car
  fields = ['name', 'manufacturer', 'horsepower']

class CarUpdate(UpdateView):
  model = Car
  fields = ['name', 'manufacturer', 'horsepower']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'


class TiresList(ListView):
  model = Tires

class TiresDetail(DetailView):
  model = Tires

class TiresCreate(CreateView):
  model = Tires
  fields = '__all__'

class TiresUpdate(UpdateView):
  model = Tires
  fields = ['name', 'origin']

class TiresDelete(DeleteView):
  model = Tires
  success_url = '/tires/'

def assoc_tire(request, car_id, tire_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Car.objects.get(id=car_id).tires.add(tire_id)
  return redirect('detail', car_id=car_id)