from django import forms

from online_shop.web.models import Contact, Testimonial


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('rating', 'comment', )