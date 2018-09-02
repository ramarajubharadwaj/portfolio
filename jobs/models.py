from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='photos/')
    summary = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.summary