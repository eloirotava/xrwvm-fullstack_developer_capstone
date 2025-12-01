# server/djangoapp/models.py
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class CarModel(models.Model):
    # Relacionamento Many-To-One: Um CarMake tem muitos CarModels
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    
    # Opções para o tipo de carro
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('SPORTS', 'Sports'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SEDAN')
    
    # Ano com validação (2015 a 2023)
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    def __str__(self):
        return self.name