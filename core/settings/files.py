from . import BASE_DIR
from .aws import AWS_STORAGE_BUCKET_NAME

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# Storages
STORAGES = {
    "default": {
        "BACKEND": DEFAULT_FILE_STORAGE,
        "OPTIONS": {
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            "location": "media",
        },
    },
    "staticfiles": {
        "BACKEND": DEFAULT_FILE_STORAGE,
        "OPTIONS": {
            "location": "static",
        },
    },
}
