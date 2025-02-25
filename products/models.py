from django.db import models

class Products(models.Model):
    name = models.TextField(max_length=60)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name