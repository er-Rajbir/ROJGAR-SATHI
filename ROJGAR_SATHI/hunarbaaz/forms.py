from django import forms
from .models import Hunarbaaz
from django.contrib.auth.models import User

class HunarbaazUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class HunarbaazProfileForm(forms.ModelForm):
    other_skill = forms.CharField(required=False, label='Other Skill')
    other_location = forms.CharField(required=False, label='Other Location')
    class Meta:
        model = Hunarbaaz
        fields = ['full_name', 'mobile', 'skill', 'location', 'experience', 'aadhaar_number', 'profile_pic','work_sample','wages']
        def clean_skill(self):
            skill = self.cleaned_data.get('skill')
            if not skill:
                raise forms.ValidationError("Please select a valid skill.")
            return skill
        def clean_aadhaar_number(self):
            aadhaar = self.cleaned_data['aadhaar_number']
            if not aadhaar.isdigit() or len(aadhaar) != 12:
                raise forms.ValidationError("Aadhaar must be exactly 12 numeric digits.")
            return aadhaar
        