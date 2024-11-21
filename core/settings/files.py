from . import BASE_DIR, DEBUG
from .aws import *
from .aws import AWS_STORAGE_BUCKET_NAME

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    BASE_DIR / "staticfiles"
]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

S3_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# Storages
STORAGES = {
    "default": {
        "BACKEND": S3_FILE_STORAGE,
        "OPTIONS": {
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "location": "media",
        },
    },
    "staticfiles": {
        "BACKEND": STATICFILES_STORAGE if DEBUG else S3_FILE_STORAGE,
        "OPTIONS": {
            "location": "static",
        },
    },
}
