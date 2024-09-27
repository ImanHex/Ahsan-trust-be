from django.db import models


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50, null=False)
    images_url = models.URLField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    time = models.CharField(max_length=50, blank=True)
    ActiveDate = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    logo = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.name}"

