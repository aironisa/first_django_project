from django.db import models

# Create your models here.
class User:
    first_name = models.CharField()
    age = models.IntegerField()