from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import TextField



class Types(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='Product')

    name = models.CharField(max_length=200)
    types = models.ForeignKey(Types, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Messages(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    types = models.TextField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.types