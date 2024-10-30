from django.urls import path
from .views import ProductRegistrationAPIView

urlpatterns = [
    path('product', ProductRegistrationAPIView.as_view(), name='register-product-api'),
]
