from django import forms
from django.contrib.auth import get_user_model

from online_shop.web.models import Contact, Testimonial, Discount

UserModel = get_user_model()


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class CreateTestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('rating', 'comment',)


class CreateDiscountForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=UserModel.objects.all(), label='User')

    class Meta:
        model = Discount
        fields = ('user', 'amount',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['class'] = 'form-control'

