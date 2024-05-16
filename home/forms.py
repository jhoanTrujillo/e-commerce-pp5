from django import forms
from home.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        error_css_class = "is-danger"
        fields = ['sender', 'email', 'subject', 'message']

        widgets = {
            'sender': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Enter name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'e.g: test@gmail.com'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'You can add a subject'
            }),
            'message': forms.TextInput(attrs={
                'class': 'textarea',
                'placeholder': 'Enter here your request'
            }),
        }
