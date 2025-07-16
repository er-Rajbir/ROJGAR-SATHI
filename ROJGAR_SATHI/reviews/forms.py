from django import forms
from .models import ContactReview

class PublicContactForm(forms.ModelForm):
    class Meta:
        model = ContactReview
        fields = ['name', 'email', 'user_type', 'query_type', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}),
            'user_type': forms.Select(attrs={'class': 'form-select'}),
            'query_type': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your message here'}),
            }
