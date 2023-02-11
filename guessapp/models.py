from django.db import models

# Create your models here.

class History(models.Model):
    number = models.PositiveIntegerField()
    attempts = models.PositiveIntegerField()
    finished_at = models.DateTimeField(auto_now_add=True)
