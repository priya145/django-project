from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    name=models.CharField(max_length=100)
    asset=models.IntegerField()
    liability=models.IntegerField()
    
    def __str__(self):
        return self.name
