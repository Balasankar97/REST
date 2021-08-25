from django.db import models


class Courses(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    ratings = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.name
