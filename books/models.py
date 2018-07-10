from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    isbn = models.BigIntegerField()
    year = models.BigIntegerField()
    author = models.CharField(max_length=100)



    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + '...'
