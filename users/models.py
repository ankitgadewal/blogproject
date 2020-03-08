from django.db import models


# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.email