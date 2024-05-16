from django import forms
from .widgets import CustomCLearableFileInput
from .models import Product, Collection, Variant


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    # Specify the upload path
    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomCLearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        collection = Collection.objects.all()
        friendly_names = [(c.id, c.get_friendly_name) for c in collection]

        self.fields['collection'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input'


class VariantForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = '__all__'

    product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                     empty_label=None,
                                     label='Product')

    # Specify the upload path
    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomCLearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input'
