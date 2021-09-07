from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Mobile_Number = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.first_name +" "+self.last_name

class Order(models.Model):
    product = models.CharField(max_length=200)
    quantity = models.IntegerField(null=False)
    customer = models.ForeignKey(Customer,related_name="orders",on_delete=models.CASCADE)

    def __str__(self):
        return self.product
