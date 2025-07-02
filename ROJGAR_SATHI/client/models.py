from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='client/profile_pics/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ClientProfile: {self.user.username}"
