from django.db import models
from datetime import datetime

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    datetime = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title