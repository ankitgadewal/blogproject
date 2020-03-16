from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confpassword = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.username

class NewBlog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.CharField(max_length=200, default='myblog')

    def __str__(self):
        return self.title