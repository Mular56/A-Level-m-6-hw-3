from django.db import models

# Create your models here.
class Book (models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    author = models.CharField(max_length=128, null=True, blank=True)