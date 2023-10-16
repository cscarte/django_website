from django.db import models


# Create your models here.

class Room(models.Model):
    #host = models.ForeignKey(User, on_delete=models.CASCADE)
    #topic = models.CharField(max_length=255)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
