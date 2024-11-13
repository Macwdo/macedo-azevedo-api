from os import getenv

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getenv("DB_NAME", "postgres"),
        "USER": getenv("DB_USER", "postgres"),
        "PASSWORD": getenv("DB_PASSWORD", "postgres"),
        "HOST": getenv("DB_HOST", "localhost"),
        "PORT": getenv("DB_PORT", 5432),
        "TEST": {
            "NAME": "test_db",
        },
    },
}


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
