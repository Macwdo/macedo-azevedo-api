from django.db import models


class Phone(models.Model):
    phone = models.CharField(max_length=20)
    ddi = models.CharField(max_length=5)
    ddd = models.CharField(max_length=5)
