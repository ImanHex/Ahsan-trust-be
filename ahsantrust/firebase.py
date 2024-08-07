import firebase_admin
from firebase_admin import credentials, storage
from django.conf import settings

if not firebase_admin._apps:
    cred = credentials.Certificate(settings.FIREBASE_ADMIN_CREDENTIALS)
    firebase_admin.initialize_app(
        cred, {"storageBucket": f"{settings.FIREBASE_STORAGE_BUCKET}.appspot.com"}
    )

bucket = storage.bucket()
