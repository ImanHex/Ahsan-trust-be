from django import forms
from .models import stores
from firebase import bucket 


class StoresAdminForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = stores
        fields = [
            "name",
            "details",
            "location",
            "categories",
            "phone",
            "time",
            "images_url",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        image = self.cleaned_data.get("image")

        if image:
            blob = bucket.blob(f"images/{image.name}")
            blob.upload_from_file(image.file, content_type=image.content_type)
            blob.make_public()
            instance.images_url = blob.public_url

        if commit:
            instance.save()
        return instance
