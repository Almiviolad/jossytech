from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    client = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

class Message(models.Model):
    name = models.CharField(max_length=300, default=None)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
