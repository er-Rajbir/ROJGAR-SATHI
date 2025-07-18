from django.db import models
from django.contrib.auth.models import User
from hunarbaaz.models import Hunarbaaz  
from django.core.validators import MinValueValidator, MaxValueValidator

from decimal import Decimal
from django.core.validators import RegexValidator
from django.utils import timezone

aadhaar_validator = RegexValidator(
    regex=r'^\d{12}$',
    message="Aadhaar number must be exactly 12 digits"
)
mobile_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="mobile number must be exactly 10 digits"
)

from django.core.validators import RegexValidator


mobile_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="mobile number must be exactly 10 digits"
)
class ClientProfile(models.Model):
    
    GENDER_CHOICES = [("","-------"),
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    work=[('','<<<--Select-->>>'),('Residential','Residential'),('Commercial','Commercial')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name=models.CharField( max_length=20,default='client fullname', blank=False)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="M",
        verbose_name="Gender",
    )

    phone = models.CharField(max_length=15, null=True, blank=True,validators=[mobile_validator])

    phone = models.CharField(max_length=10,unique=True,validators=[mobile_validator])

    address = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='client/profile_pics/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ClientProfile: {self.user.username}"
    
class PostRequest(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    hunarbaaz = models.ForeignKey('hunarbaaz.Hunarbaaz', on_delete=models.CASCADE, related_name='received_requests')

    job_description = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateField(help_text="Start date of the job",null=False,blank=True)
    end_date = models.DateField(help_text="Expected completion date",null=False,blank=True)
    JOB_TYPE_CHOICES = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
    ]

    job_type = models.CharField(max_length=20,choices=JOB_TYPE_CHOICES,default='residential',help_text="Type of job location")
    working_hours = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Estimated total working hours for this job"
    )
    is_accepted = models.BooleanField(null=True, blank=True)  # None = Pending, True = Accepted, False = Rejected
    is_completed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False, help_text="Whether the client has cancelled the request")



    created_at = models.DateTimeField(auto_now_add=True)

    # ⭐ Rating and Review (1.0 to 5.0 with one decimal place)
    rating = models.IntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(5)],
    null=True,
    blank=True,
    help_text="Client rating after completion (1 to 5)"
)
    review = models.TextField(null=True, blank=True, help_text="Optional client feedback")

    def __str__(self):
        return f"Request from {self.client.username} to {self.hunarbaaz.full_name}"
