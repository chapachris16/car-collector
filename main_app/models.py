from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.

FUELS = (
    ('A', 'Regular Unleaded' ),
    ('B', 'Premium Unleaded'),
    ('C', 'Supreme Unleaded'),
    ('E', 'Ethanol Fuel')
)

class Tires(models.Model):
    name = models.CharField(max_length=35)
    origin = models.CharField(max_length=35)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tires_detail', kwargs={'pk': self.id})




class Car(models.Model):
    name = models.CharField(max_length=35)
    manufacturer = models.CharField(max_length=35)
    horsepower = models.IntegerField()
    tires = models.ManyToManyField(Tires)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Fueling(models.Model):
  date = models.DateField('Date Fueled:')
  fuel = models.CharField(
    'Fuel Types',
    max_length=1,
    choices=FUELS,
    default=FUELS[0][0]
  )
  # create a cat_id column in the db
  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_fuel_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
