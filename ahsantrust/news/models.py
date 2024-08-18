from django.db import models


# Create your models here.
class news(models.Model):
    name = models.CharField(max_length=100, null=False)
    details = models.CharField(max_length=2000, blank=True)
    Date = models.DateTimeField(max_length=50, null=False)
    image = models.CharField(max_length=500, blank=True)


def __str__(self):
    return f"{self.name} - {self.details} - {self.Date}- {self.image}"
