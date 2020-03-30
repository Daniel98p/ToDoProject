from django.db import models
from datetime import date


class ToDoText(models.Model):
    text = models.CharField(max_length=300)
    data = models.DateField(default=date.today)
    
