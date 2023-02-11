# api/models.py
from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    work = models.ManyToManyField('Work', blank=True)

class Work(models.Model):
    link = models.URLField()
    WORK_TYPE_CHOICES = [
        ('youtube', 'Youtube'),
        ('instagram', 'Instagram'),
        ('other', 'Other'),
    ]
    work_type = models.CharField(max_length=10, choices=WORK_TYPE_CHOICES)

