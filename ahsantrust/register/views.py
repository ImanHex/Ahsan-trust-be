from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.mail import EmailMessage
from django.conf import settings
from rest_framework import status

class FileUploadTestAPIView(APIView):
    permission_classes = [AllowAny]  # Allow unrestricted access (no model permissions)
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        logo = request.FILES.get('logo')
        product_image = request.FILES.get('product_image')

        print(f"Logo: {logo}")
        print(f"Product Image: {product_image}")

        if logo and product_image:
            return Response({"message": "Both files received!"})
        return Response({"message": "Some files are missing."}, status=400)

class ProductRegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # Extract data from the request
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone_number = request.data.get('phone_number')
        store_name = request.data.get('store_name')
        store_location = request.data.get('store_location')
        logo = request.FILES.get('logo')  # File (if provided)
        product_name = request.data.get('product_name')
        product_description = request.data.get('product_description')
        product_image = request.FILES.get('product_image')  # Required file

        # Prepare email content
        subject = f"New Product Registration by {first_name} {last_name}"
        message = (
            f"Product Name: {product_name}\n"
            f"Description: {product_description}\n"
            f"Store: {store_name}\n"
            f"Phone: {phone_number}\n"
            f"Location: {store_location}"
        )
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['ahsantrustmark67@gmail.com']

        email = EmailMessage(subject, message, from_email, recipient_list)

        if logo:
            email.attach(logo.name, logo.read(), logo.content_type)

        if product_image:
            email.attach(product_image.name, product_image.read(), product_image.content_type)

        print(f"Logo: {logo}")
        print(f"Product Image: {product_image}")

        print(request.data)  # Print all form data
        print(request.FILES)

        # Send the email
        email.send()

        return Response({"message": "Product registration email sent successfully!"}, status=status.HTTP_200_OK)

