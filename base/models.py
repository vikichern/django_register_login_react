from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
