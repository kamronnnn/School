from django.db import models

# Create your models here.


class Clas(models.Model):
    name = models.CharField(max_length=50)


class Teacher(models.Model):
    fullname = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    clas = models.ManyToManyField(Clas)


class Student(models.Model):
    fullname = models.CharField(max_length=50)
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE)




