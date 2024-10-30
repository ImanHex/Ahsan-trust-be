# views.py
import datetime

from firebase import bucket
from .admin import criteria_structure
from .models import ProductRegistration
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework import status
import json

class ProductRegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser)

    def upload_to_firebase(self, file, folder_name):
        # Generate a unique filename
        filename = f"{folder_name}/{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{file.name}"
        blob = bucket.blob(filename)
        blob.upload_from_file(file, content_type=file.content_type)
        # Make URL publicly accessible
        blob.make_public()
        return blob.public_url

    def post(self, request, *args, **kwargs):
        # Extract data from the request
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone_number = request.data.get('phone_number')
        store_name = request.data.get('store_name')
        store_location = request.data.get('store_location')
        logo = request.FILES.get('logo')
        product_name = request.data.get('product_name')
        product_description = request.data.get('product_description')
        product_image = request.FILES.get('product_image')

        # Parse criteria JSON data
        criteria_json = request.data.get('criteria')
        print("Raw criteria JSON:", criteria_json)

        logo_url, product_image_url = None, None
        if 'logo' in request.FILES:
            logo_url = self.upload_to_firebase(request.FILES['logo'], 'logos')
        if 'product_image' in request.FILES:
            product_image_url = self.upload_to_firebase(request.FILES['product_image'], 'product_images')

        try:
            criteria = json.loads(criteria_json) if criteria_json else {}
            print("Parsed criteria:", criteria)  # Log parsed criteria
        except json.JSONDecodeError:
            print("Failed to parse criteria JSON")
            return Response({"error": "Invalid criteria format"}, status=status.HTTP_400_BAD_REQUEST)

        # Log all data right before saving
        print("Data ready for saving:")
        print("first_name:", first_name)
        print("last_name:", last_name)
        print("phone_number:", phone_number)
        print("store_name:", store_name)
        print("store_location:", store_location)
        print("product_name:", product_name)
        print("product_description:", product_description)
        print("criteria:", criteria)

        # Save to the database
        registration = ProductRegistration.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            store_name=store_name,
            store_location=store_location,
            logo=logo,
            product_name=product_name,
            product_description=product_description,
            product_image=product_image,
            selected_criteria=criteria  # Save criteria in JSON format
        )

        # Prepare criteria table for the email
        criteria_table = "<table border='1' cellpadding='5' cellspacing='0'><tr><th>Criteria</th><th>Mark</th></tr>"
        for category_key, category_data in criteria_structure.items():
            criteria_table += f"<tr><td colspan='2' style='font-weight: bold; background-color: #f0f0f0;'>{category_data['label']}</td></tr>"
            for sub_key, sub_label in category_data["sub_criteria"].items():
                selected = criteria.get(sub_key, False)
                mark = "✔" if selected else "✘"
                criteria_table += f"<tr><td>{sub_label}</td><td style='text-align: center;'>{mark}</td></tr>"
        criteria_table += "</table>"

        # Prepare email content
        subject = f"New Product Registration by {first_name} {last_name}"
        message = (
            f"<p>Product Name: {product_name}</p>"
            f"<p>Description: {product_description}</p>"
            f"<p>Store: {store_name}</p>"
            f"<p>Phone: {phone_number}</p>"
            f"<p>Location: {store_location}</p><br>"
            f"<h3>Criteria:</h3>{criteria_table}"
            f"<p><strong>Logo:</strong> <br><img src='{logo_url}' width='200'></p>"
            f"<p><strong>Product Image:</strong> <br><img src='{product_image_url}' width='200'></p>"
        )
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['ahsantrustmark67@gmail.com']

        email = EmailMessage(subject, message, from_email, recipient_list)
        email.content_subtype = "html"

        # Attach files if provided
        if logo:
            email.attach(logo.name, logo.read(), logo.content_type)
        if product_image:
            email.attach(product_image.name, product_image.read(), product_image.content_type)

        # Send the email
        email.send()

        return Response({"message": "Product registered successfully!"}, status=status.HTTP_201_CREATED)
