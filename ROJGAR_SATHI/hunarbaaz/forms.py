from django import forms
from .models import Hunarbaaz
from django.contrib.auth.models import User

class HunarbaazUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
class HunarbaazProfileForm(forms.ModelForm):
    other_skill = forms.CharField(required=False, label='Other Skill')
    other_location = forms.CharField(required=False, label='Other Location')
    skill = forms.ChoiceField(
        choices=Hunarbaaz.SKILL_CHOICES,
        widget=forms.Select(attrs={'id': 'id_skill'})   # ← add id here
    )
    wages = forms.IntegerField(label="Wages (₹ / 8 hrs) *",
        help_text="These wages are determined by the platform and are not manually editable.",
        widget=forms.NumberInput(attrs={'id': 'id_wages',  "readonly": "readonly", 'min': 0})
    )
    gender = forms.ChoiceField(
        choices=Hunarbaaz.GENDER_CHOICES,   # or forms.Select for a drop‑down
        label="Gender"
    )
    
    class Meta:
        model = Hunarbaaz
        fields = ['full_name', 'mobile', 'gender', 'skill', 'location', 'experience', 'aadhaar_number', 'profile_pic','work_sample_1','work_sample_2','work_sample_3','wages']
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
        def clean_mobile(self):
                mobilee = self.cleaned_data['mobile']
                if not mobilee.isdigit() or len(mobilee) != 10:
                    raise forms.ValidationError("mobile must be exactly 10 numeric digits.")
                return mobilee
        