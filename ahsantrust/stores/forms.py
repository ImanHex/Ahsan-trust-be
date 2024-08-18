from django import forms
from .models import stores
from firebase import bucket

VALUES_CHOICES = [
    ("Local Lifestyle Value (คุณค่าวิถีท้องถิ่น)", "Local Lifestyle Value (คุณค่าวิถีท้องถิ่น)"),
    ("Local Wisdom value (คุณค่าภูมิปัญญาท้องถิ่น)", "Local Wisdom Value (คุณค่าภูมิปัญญาท้องถิ่น)"),
    (
        "Community Support Value (คุณค่าการสนับสนุนชุมชน)",
        "Community Support Value (คุณค่าการสนับสนุนชุมชน)",
    ),
]

QUALITIES_CHOICES = [
    (
        "Quality of Raw Materials (คุณภาพของวัตถุดิบ)",
        "Quality of Raw Materials (คุณภาพของวัตถุดิบ)",
    ),
    (
        "Product Safety Quality (คุณภาพความปลอดภัยของผลิตภัณฑ์)",
        "Product Safety Quality (คุณภาพความปลอดภัยของผลิตภัณฑ์)",
    ),
]

ETHICS_CHOICES = [
    (
        "Fairness Ethics (คุณธรรมในการไม่เอาเปรียบผู้ผลิต-ผู้ประกอบการ-ผู้บริโภค)",
        "Fairness Ethics (คุณธรรมในการไม่เอาเปรียบผู้ผลิต-ผู้ประกอบการ-ผู้บริโภค)",
    ),
    (
        "Islamic Compliance Ethics (ธรรมในการปฏิบัติตามหลักศาสนาอิสลาม)",
        "Islamic Compliance Ethics (ธรรมในการปฏิบัติตามหลักศาสนาอิสลาม)",
    ),
    (
        "Environmental Ethics (คุณธรรมในการรักษาสิ่งแวดล้อม)",
        "Environmental Ethics (คุณธรรมในการรักษาสิ่งแวดล้อม)",
    ),
    (
        "Local Labor Support Ethics (คุณธรรมในการสนับสนุนแรงงานท้องถิ่น)",
        "Local Labor Support Ethics (คุณธรรมในการสนับสนุนแรงงานท้องถิ่น)",
    ),
]

BENEFITS_CHOICES = [
    ("Health Benefits (ประโยชน์ต่อสุขภาพ)", "Health Benefits (ประโยชน์ต่อสุขภาพ)"),
    ("Social Benefits (ประโยชน์ทางสังคม)", "Social Benefits (ประโยชน์ทางสังคม)"),
    ("Charity and Zakat (การบริจาคและซะกาต)", "Charity and Zakat (การบริจาคและซะกาต)"),
]


class StoresAdminForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    logo_image = forms.ImageField(required=False)
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
        model = stores
        fields = [
            "name",
            "details",
            "location",
            "categories",
            "phone",
            "time",
            "images_url",
            "logo",
            "values",
            "qualities",
            "ethics",
            "benefits",
            "facebook",
            "instagram",
            "ActiveDate",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        image = self.cleaned_data.get("image")

        if image:
            blob = bucket.blob(f"images/{image.name}")
            blob.upload_from_file(image.file, content_type=image.content_type)
            blob.make_public()
            instance.images_url = blob.public_url

        logo_image = self.cleaned_data.get("logo_image")
        if logo_image:
            blob = bucket.blob(f"logos/{logo_image.name}")
            blob.upload_from_file(logo_image.file, content_type=logo_image.content_type)
            blob.make_public()
            instance.logo = blob.public_url

        instance.values = self.cleaned_data.get("values", [])
        instance.qualities = self.cleaned_data.get("qualities", [])
        instance.ethics = self.cleaned_data.get("ethics", [])
        instance.benefits = self.cleaned_data.get("benefits", [])

        if commit:
            instance.save()
        return instance
