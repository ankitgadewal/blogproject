from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.CharField(max_length=200, default='myblog')

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    datetime = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.comment

