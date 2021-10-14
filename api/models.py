from django.db import models


class Product(models.Model):
    name= models.CharField(max_length=100)
    price= models.IntegerField()
    description=models.DateField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        ordering=["name"]
