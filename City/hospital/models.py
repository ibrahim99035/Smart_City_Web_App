from django.db import models

# Create your models here.
class Employee(models.Model):
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=40)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=255)
    natId = models.CharField(max_length=14)

class Patient(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=40)
    psatHistory = models.CharField(max_length=350)
    age = models.IntegerField() 
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=255)
    natId = models.CharField(max_length=14)
    admissionDate = models.DateTimeField

class Departments(models.Model):
    Title = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    