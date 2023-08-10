from django import forms

from online_shop.products.models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'description': forms.Textarea(),
        }


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'description': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].required = False
        self.fields['name'].widget.attrs['placeholder'] = "Enter product name"

        self.fields['description'].required = False
        self.fields['description'].widget.attrs['placeholder'] = "Enter product description"

        self.fields['price'].required = False
        self.fields['price'].widget.attrs['placeholder'] = "Enter product price"

        self.fields['photo'].required = False
