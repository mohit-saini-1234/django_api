from django.db import models
from datetime import datetime
# Create your models here.
from django.db import models

# Create your models here.

class Todo(models.Model):
    email = models.EmailField(max_length=70, null=True, blank=False, unique=True)
    task = models.CharField(max_length=255)
    description = models.TextField(default="")
    priority = models.IntegerField(default=1)
    created = models.DateTimeField(default=datetime.now,blank=True) 