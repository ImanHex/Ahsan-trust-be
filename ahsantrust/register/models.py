# models.py
from django.db import models


class ProductRegistration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    store_name = models.CharField(max_length=100, blank=True, null=True)
    store_location = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)  # Optional
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(blank=True, null=True)
    product_image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    selected_criteria = models.JSONField()
    # status = models.CharField(max_length=10 )

    def __str__(self):
        return f"{self.first_name} - {self.product_name}"
