from django import forms
from .models import Store
from firebase import bucket

class StoresAdminForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    logo_image = forms.ImageField(required=False)


    class Meta:
        model = Store
        fields = [
            "name",
            "location",
            "phone",
            "time",
            "facebook",
            "instagram",
            "ActiveDate",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        image = self.cleaned_data.get("image")

        if image:
            blob = bucket.blob(f"stores/{image.name}")
            blob.upload_from_file(image.file, content_type=image.content_type)
            blob.make_public()
            instance.images_url = blob.public_url

        logo_image = self.cleaned_data.get("logo_image")
        if logo_image:
            blob = bucket.blob(f"logos/{logo_image.name}")
            blob.upload_from_file(logo_image.file, content_type=logo_image.content_type)
            blob.make_public()
            instance.logo = blob.public_url



        if commit:
            instance.save()
        return instance
