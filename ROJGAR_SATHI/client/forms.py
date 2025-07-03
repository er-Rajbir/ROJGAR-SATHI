from django import forms
from django.contrib.auth.models import User
from .models import ClientProfile, PostRequest

class ClientRegisterForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = ['phone', 'address', 'company_name', 'profile_picture']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class PostRequestForm(forms.ModelForm):
    class Meta:
        model = PostRequest
        fields = ['hunarbaaz', 'job_description', 'location', 'scheduled_date']
        widgets = {
            'scheduled_date': forms.DateInput(attrs={'type': 'date'}),
            'job_description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(PostRequestForm, self).__init__(*args, **kwargs)
        if self.initial.get('hunarbaaz'):
            self.fields['hunarbaaz'].widget = forms.HiddenInput()
