from django.db import models
from datetime import datetime

class Content(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.subject[:50]

