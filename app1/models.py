from typing import Any
from django.db import models


# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.TextField(max_length=100)
    
        
    
    def __str__(self):
        return self.name
        
        