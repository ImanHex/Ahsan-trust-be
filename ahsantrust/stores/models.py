from django.db import models


# Create your models here.
class stores(models.Model):
    name = models.CharField(max_length=50, null=False)
    images_url = models.URLField(max_length=500, blank=True)
    details = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    categories = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    time = models.CharField(max_length=50, blank=True)


def __str__(self):
    return f"{self.name} - {self.details} - {self.location}- {self.categories}- {self.time}- {self.images_url}"
