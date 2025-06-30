from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=10)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name

class Cereal(models.Model):
    name = models.CharField(max_length=100)
    mfr = models.CharField(max_length=1)  # Manufacturer (single letter)
    type = models.CharField(max_length=1)  # Type (C=Cold, H=Hot)
    calories = models.IntegerField()
    protein = models.FloatField()
    fat = models.FloatField()
    sodium = models.FloatField()
    fiber = models.FloatField()
    carbo = models.FloatField()
    sugars = models.FloatField()
    potass = models.FloatField()
    vitamins = models.FloatField()
    shelf = models.IntegerField()
    weight = models.FloatField()
    cups = models.FloatField()
    rating = models.FloatField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cereals"
