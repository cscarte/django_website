from django.db import models


# Create your models here.

class Room(models.Model):
    # host = models.ForeignKey(User, on_delete=models.CASCADE)
    # topic = models.CharField(max_length=255)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, max_length=5000)
    # participants = models.ManyToManyField('Participant', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
