from django import forms

from online_shop.web.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
