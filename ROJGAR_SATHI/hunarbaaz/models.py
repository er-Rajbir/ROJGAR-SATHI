from django.db import models
from django.contrib.auth.models import User

class Hunarbaaz(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    skill = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    aadhaar_number = models.CharField(max_length=12, unique=True)
    profile_pic = models.ImageField(upload_to='hunarbaaz/profile_pics/', null=True, blank=True)
    work_sample = models.ImageField(upload_to='hunarbaaz/work_samples/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.full_name