from django.db import models
from django.core.validators import FileExtensionValidator

class bloginfo(models.Model):
    name = models.CharField(max_length=20)
    details = models.CharField(max_length=200)
    date = models.DateField()
    url = models.URLField(max_length=200)
    def __str__(self):
        return self.name






# Create your models here.
