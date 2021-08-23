from django.db import models

# Create your models here.

class Passenger(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    start_point = models.CharField(max_length=20)
    end_point = models.CharField(max_length=20)

    def __str__(self):
        return self.name
