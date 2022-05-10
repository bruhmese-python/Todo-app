from django.db import models
import datetime
# Create your models here.


class Task(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    priority = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(default=datetime.date.today)
