import datetime
from django.db import models
from django.db.models.fields import CharField, TimeField
class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    dob = models.DateField()
    mail = models.EmailField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
class AccRequest(models.Model):    
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    dob = models.DateField()
    mail = models.EmailField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    access = models.CharField(max_length=10)

