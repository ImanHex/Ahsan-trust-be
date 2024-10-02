from django import forms
from .models import Product, ProductImage
from firebase import bucket
import logging
logger = logging.getLogger(__name__)

VALUES_CHOICES = [
    ("Local Lifestyle Value", "Local Lifestyle Value"),
    ("Local Wisdom value", "Local Wisdom value"),
    ("Community Support Value", "Community Support Value"),
]

QUALITIES_CHOICES = [
    ("Quality of Raw Materials", "Quality of Raw Materials"),
    ("Product Safety Quality", "Product Safety Quality"),
    ("Consistency of Product","Consistency of Product")
]

ETHICS_CHOICES = [
    ("Fairness Ethics", "Fairness Ethics"),
    ("Islamic Compliance Ethics", "Islamic Compliance Ethics"),
    ("Environmental Ethics", "Environmental Ethics"),
    ("Local Labor Support Ethics", "Local Labor Support Ethics"),
]

BENEFITS_CHOICES = [
    ("Health Benefits", "Health Benefits"),
    ("Social Benefits", "Social Benefits"),
    ("Charity and Zakat", "Charity and Zakat"),
]

class ProductImageForm(forms.ModelForm):
    image = forms.ImageField(required=False)  # Allow file uploads

    class Meta:
        model = ProductImage
        fields = ['image']  # Only need the image field

    def save(self, commit=True):
        instance = super().save(commit=False)
        image = self.cleaned_data.get("image")

        if image:
            logger.info(f"Image found: {image.name}")
            try:
                # Log the start of the upload process
                logger.info(f"Uploading image: {image.name} to Firebase")

                # Upload image to Firebase
                blob = bucket.blob(f"products/{image.name}")
                blob.upload_from_file(image.file, content_type=image.content_type)
                blob.make_public()

                # Save public URL to the model
                instance.image_url = blob.public_url
                logger.info(f"Image uploaded successfully: {instance.image_url}")
            except Exception as e:
                logger.error(f"Error uploading image to Firebase: {e}")
                raise forms.ValidationError("Image upload failed. Please try again.")
        else:
            logger.warning("No image was found in the form submission.")

        if commit:
            instance.save()
        return instance




class ProductAdminForm(forms.ModelForm):

    values = forms.MultipleChoiceField(
        choices=VALUES_CHOICES, required=False, widget=forms.CheckboxSelectMultiple
    )
    qualities = forms.MultipleChoiceField(
        choices=QUALITIES_CHOICES, required=False, widget=forms.CheckboxSelectMultiple
    )
    ethics = forms.MultipleChoiceField(
        choices=ETHICS_CHOICES, required=False, widget=forms.CheckboxSelectMultiple
    )
    benefits = forms.MultipleChoiceField(
        choices=BENEFITS_CHOICES, required=False, widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Product
        fields = [
            "store",
            "name",
            "details",
            "categories",
            "values",
            "qualities",
            "ethics",
            "benefits",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.values = self.cleaned_data.get("values", [])
        instance.qualities = self.cleaned_data.get("qualities", [])
        instance.ethics = self.cleaned_data.get("ethics", [])
        instance.benefits = self.cleaned_data.get("benefits", [])
        if commit:
            instance.save()
        return instance
