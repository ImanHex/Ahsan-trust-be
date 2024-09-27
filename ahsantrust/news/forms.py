from django import forms
from .models import news
from firebase import bucket


class NewsAdminForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = news
        fields = ["name", "details", "image", "Date"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        image = self.cleaned_data.get("image")

        if image and not isinstance(image, str):
            blob = bucket.blob(f"newsImg/{image.name}")
            blob.upload_from_file(image.file, content_type=image.content_type)
            blob.make_public()
            instance.image = blob.public_url
        elif isinstance(instance.image, str):
            # If image is already a URL (string), keep it unchanged
            instance.image = instance.image
        else:
            # If no new image is provided, keep the existing one
            instance.image = instance.image

        if commit:
            instance.save()
        return instance
