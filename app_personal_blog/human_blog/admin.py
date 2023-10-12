#
#
#
from django.contrib import admin
from .models import ContactModel, Newsletter

admin.site.register(ContactModel)
admin.site.register(Newsletter)
