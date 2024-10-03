from django import forms

class ProductRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    store_name = forms.CharField(max_length=100)
    store_location = forms.CharField(max_length=255)
    logo = forms.ImageField(required=False)  # Optional
    product_name = forms.CharField(max_length=100)
    product_description = forms.CharField(widget=forms.Textarea)
    product_image = forms.ImageField(required=False)