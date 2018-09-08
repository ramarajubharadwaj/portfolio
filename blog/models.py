from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    body = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='blog/pictures/')
    
    def __str__(self):
        return self.title

