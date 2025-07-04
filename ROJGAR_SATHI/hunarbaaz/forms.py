from django import forms
from .models import Hunarbaaz
from django.contrib.auth.models import User

class HunarbaazUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class HunarbaazProfileForm(forms.ModelForm):
    class Meta:
        model = Hunarbaaz
        fields = ['full_name', 'mobile', 'skill', 'location', 'experience', 'aadhaar_number', 'profile_pic','work_sample']
        def clean_skill(self):
            skill = self.cleaned_data.get('skill')
            if not skill:
                raise forms.ValidationError("Please select a valid skill.")
            return skill
