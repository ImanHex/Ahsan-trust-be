from django import forms
from .models import announce
from firebase import bucket


class AnnounceAdminForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = announce
        fields = ["title",'description', 'date','time','location','register_link','image']

    def save(self, commit=True):
        instance = super().save(commit=False)
        image = self.cleaned_data.get("image")  # Get the image from the form

        if image:
            if not isinstance(image, str):  # A new image file is uploaded
                blob = bucket.blob(f"AnnounceImg/{image.name}")
                blob.upload_from_file(image.file, content_type=image.content_type)
                blob.make_public()
                instance.image = blob.public_url  # Update instance.image with the new URL
        elif not image and instance.pk:  # No new image provided; keep the existing image if the instance already exists
            instance.image = instance.image
        else:
            instance.image = None  # No image provided for new instances

        if commit:
            instance.save()
        return instance

