from django.db import models
from django.core.validators import FileExtensionValidator

class proj(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title
