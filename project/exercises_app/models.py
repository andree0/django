from django.db import models


# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
