from django.db import models


class Customer(models.Model):
    name = models.CharField("name", max_length=100)

    def __str__(self):
        return self.name


class Data(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField("date")
    total = models.PositiveIntegerField("total", default=0)
    quantity = models.PositiveSmallIntegerField("quantity", default=0)
    item = models.CharField("item", max_length=100)
