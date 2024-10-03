from django.urls import path
from .views import ProductRegistrationAPIView, FileUploadTestAPIView

urlpatterns = [
    path('product', ProductRegistrationAPIView.as_view(), name='register-product-api'),
    path('test', FileUploadTestAPIView.as_view(), name='register-product-test'),
]
