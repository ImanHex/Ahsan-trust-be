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

        if isinstance(image, forms.ImageField):  # Check if image is actually a file
            # Upload the new image to Firebase
            blob = bucket.blob(f"newsImg/{image.name}")
            blob.upload_from_file(image.file, content_type=image.content_type)
            blob.make_public()
            instance.image = blob.public_url
        else:

            instance.image = instance.image

        if commit:
            instance.save()
        return instance
