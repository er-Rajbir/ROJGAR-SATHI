from django import forms
from django.contrib.auth.models import User
from .models import ClientProfile, PostRequest, Hunarbaaz

class ClientRegisterForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password',]


class ClientProfileForm(forms.ModelForm):
    full_name = forms.CharField(max_length=20, required=True)
    gender = forms.ChoiceField(
        choices=ClientProfile.GENDER_CHOICES,   # or forms.Select for a drop‑down
        label="Gender"
    )
    class Meta:
        model = ClientProfile
        fields = ['full_name','phone','gender', 'address', 'profile_picture']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        

class PostRequestForm(forms.ModelForm):
    class Meta:
        model = PostRequest
        fields = [
            'hunarbaaz',
            'location',
            'start_date',
            'end_date',
            'job_type',
            'job_description',
            'working_hours',
        ]
        widgets = {
            'hunarbaaz': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'job_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'working_hours': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostRequestForm, self).__init__(*args, **kwargs)
        self.fields['hunarbaaz'].queryset = Hunarbaaz.objects.all()
        self.fields['hunarbaaz'].label_from_instance = lambda obj: obj.full_name
    
    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")
        if start and end and start > end:
            raise forms.ValidationError("End date cannot be earlier than start date.")
        return cleaned_data

class RescheduleRequestForm(forms.ModelForm):
    class Meta:
        model = PostRequest
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")
        if start and end and start > end:
            raise forms.ValidationError("End date cannot be earlier than start date.")
        return cleaned_data
    

class ReviewForm(forms.ModelForm):
    class Meta:
        model = PostRequest
        fields = ['rating', 'review']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'step': 1,  # ⬅ only integer step
                'class': 'form-control'
            }),
            'review': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control'
            }),
        }
