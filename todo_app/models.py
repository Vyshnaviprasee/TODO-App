from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

