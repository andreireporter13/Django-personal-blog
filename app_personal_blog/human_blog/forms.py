#
#
#
#
#
from django import forms
from .models import ContactModel


class MesajForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['nume', 'email', 'mesaj']
