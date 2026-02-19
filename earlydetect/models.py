from django.db import models
import uuid

class StressSession(models.Model):
    session_id = models.CharField(max_length=8, unique=True)
    category = models.CharField(max_length=20)
    score = models.IntegerField()
    percent = models.FloatField()
    level = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.session_id} - {self.level}"
