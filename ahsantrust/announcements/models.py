from django.db import models

class announce(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.CharField(max_length=255, null=True, blank=True)  # Allows blank and null values
    time = models.CharField(max_length=255, null=True, blank=True)  # Allows blank and null values
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title