from django import forms

from products.models import Product


class ProductForm(forms.ModelForm):

    image_url = forms.ImageField(widget=forms.FileInput())

    class Meta:

        model = Product
        exclude = ['created_date','modified_date','deleted_date','deleted', 'tags']