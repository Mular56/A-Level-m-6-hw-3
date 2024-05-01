from django.db import models
from django.contrib.auth.models import AbstractUser


class Comment(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    

class MyUser(AbstractUser):
    birth_date = models.DateField()
    avatar = models.ImageField(blank=True, null=True)
    
    
class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Чоловік'),
        ('F', 'Жінка'),
    ]

    ENGLISH_LEVEL_CHOICES = [
        ('A1', 'Початковий рівень (A1)'),
        ('A2', 'Елементарний рівень (A2)'),
        ('B1', 'Середній рівень (B1)'),
        ('B2', 'Високий рівень (B2)'),
        ('C1', 'Досконалий рівень (C1)'),
        ('C2', 'Високий досконалий рівень (C2)'),
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    english_level = models.CharField(max_length=2, choices=ENGLISH_LEVEL_CHOICES)