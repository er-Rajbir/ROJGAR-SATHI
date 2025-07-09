from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

aadhaar_validator = RegexValidator(
    regex=r'^\d{12}$',
    message="Aadhaar number must be exactly 12 digits"
)

class Hunarbaaz(models.Model):
    SKILL_CHOICES = [
        ('', 'Tell us your skill'),  # placeholder
        ('Construction', 'Construction'),
        ('Electrician', 'Electrician'),
        ('Painter', 'Painter'),
        ('Domestic Worker', 'Domestic Worker'),
        ('Plumber', 'Plumber'),
        ('Carpenter', 'Carpenter'),
        ('Electronics Repair', 'Electronics Repair'),
        ('Mechanic', 'Mechanic'),
        ('Others', 'Others'),
    ]
    locations=[
        ('','select you location'),
        ('Vallah/Verka','Vallah/Verka'),
        ('Hall Bazaar','Hall Bazaar'),
        ('Ranjit-Avenue','Ranjit-Avenue'),
        ('Company-bagh','Company-bagh'),
        ('Golden-gate','Golden-gate'),
        ('Putlighar','Putlighar'),
        ('Ramgharia gate','Ramgharia gate'),
        ('Batala-road','Batala-road'),
        ('Majitha-road','Majitha-road'),
        ('Ram Bagh','Ram Bagh'),
        ('other','other')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password_plain = models.CharField(max_length=128, blank=True, null=True)
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    skill = models.CharField(max_length=50, choices=SKILL_CHOICES)
    location = models.CharField(max_length=100, choices=locations)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    aadhaar_number = models.CharField(max_length=12,unique=True,validators=[aadhaar_validator])
    wages = models.PositiveIntegerField(help_text="required pay for 8 hours" ,blank=False,null=False, default=False)
    profile_pic = models.ImageField(upload_to='hunarbaaz/profile_pics/', null=True, blank=True)
    work_sample = models.ImageField(upload_to='hunarbaaz/work_samples/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class WorkRequest(models.Model):
    client_name = models.CharField(max_length=100)
    hunarbaaz = models.ForeignKey(Hunarbaaz, on_delete=models.CASCADE, related_name='work_requests')
    description = models.TextField()
    status_choices = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.client_name} to {self.hunarbaaz.full_name}"