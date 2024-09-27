from django.db import models
from firebase import bucket
from stores.models import Store
import logging
logger = logging.getLogger(__name__)
# Create your models here.
class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=50, blank=False)
    details = models.CharField(max_length=500, blank=True)
    categories = models.CharField(max_length=50, blank=True)
    values = models.JSONField(blank=True, default=list)
    qualities = models.JSONField(blank=True, default=list)
    ethics = models.JSONField(blank=True, default=list)
    benefits = models.JSONField(blank=True, default=list)

    def __str__(self):
        return f"{self.name} - {self.store.name}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return f"Image for {self.product.name}"

    def delete(self, *args, **kwargs):
        # Delete the image from Firebase before deleting the record in the database
        try:
            # Extract the Firebase file path from the image URL
            blob_name = self.image_url.split('/')[-1]  # Adjust as necessary to extract the path

            # Get the blob reference
            blob = bucket.blob(f"products/{blob_name}")

            # Delete the image from Firebase
            blob.delete()
            logger.info(f"Image {self.image_url} deleted from Firebase.")
        except Exception as e:
            logger.error(f"Error deleting image from Firebase: {e}")

        # Now delete the record from the database
        super().delete(*args, **kwargs)
