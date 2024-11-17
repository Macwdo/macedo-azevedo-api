from . import BASE_DIR
from .aws import AWS_STORAGE_BUCKET_NAME

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

S3_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATIC_FILE_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

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
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        "OPTIONS": {
            "location": "static",
        },
    },
}
