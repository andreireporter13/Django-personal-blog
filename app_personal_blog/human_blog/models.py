#
#
#
#
from django.db import models


class ContactModel(models.Model):
    nume = models.CharField(max_length=255)
    email = models.EmailField()
    mesaj = models.TextField()

    def __str__(self):
        return self.nume


class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
