from lib2to3.pgen2 import driver
from unittest.util import _MAX_LENGTH
from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.name
