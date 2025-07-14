from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

aadhaar_validator = RegexValidator(
    regex=r'^\d{12}$',
    message="Aadhaar number must be exactly 12 digits"
)
mobile_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="mobile number must be exactly 10 digits"
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
        ('','Select you location'),
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
    GENDER_CHOICES = [("","-------"),
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12,unique=True,validators=[mobile_validator])
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="M",
        verbose_name="Gender",
    )
    skill = models.CharField(max_length=50, choices=SKILL_CHOICES)
    location = models.CharField(max_length=100, choices=locations)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    aadhaar_number = models.CharField(max_length=12,unique=True,validators=[aadhaar_validator])
    wages = models.PositiveIntegerField(help_text="required pay for 8 hours" ,blank=False,null=False, default=False)
    profile_pic = models.ImageField(upload_to='hunarbaaz/profile_pics/',null=True, blank=True)
    work_sample_1=models.ImageField(upload_to='hunarbaaz/work_samples/', null=True, blank=True)
    work_sample_2=models.ImageField(upload_to='hunarbaaz/work_samples/', null=True, blank=True)
    work_sample_3=models.ImageField(upload_to='hunarbaaz/work_samples/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class WorkRequest(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work_requests',null=True, blank=True)
    hunarbaaz = models.ForeignKey('hunarbaaz.Hunarbaaz', on_delete=models.CASCADE, related_name='work_requests')

    description = models.TextField()
    location = models.CharField(max_length=100)

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    JOB_TYPE_CHOICES = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
    ]
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='residential')

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    rating = models.IntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(5)],
    null=True,
    blank=True,
    help_text="Client rating after completion (1 to 5)"
)
    review = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.client.username} to {self.hunarbaaz.full_name}"