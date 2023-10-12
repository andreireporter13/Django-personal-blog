#
#
#
#
#
from django import forms
from .models import ContactModel
from .models import Newsletter


class MesajForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['nume', 'email', 'mesaj']


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
