from django.db import models

# Create your models here.

class List(models.Model):
    activity = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    time = models.DateTimeField()

    def __str__(self):
        return self.activity
