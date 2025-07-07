from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from hunarbaaz.models import Hunarbaaz  # assuming this exists


class ClientProfile(models.Model):
    work=[('','<<<--Select-->>>'),('Residential','Residential'),('Commercial','Commercial')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name=models.CharField( max_length=20,default='client fullname', blank=False)

    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    work_type = models.CharField(max_length=20, default='N/A' ,choices=work )
    profile_picture = models.ImageField(upload_to='client/profile_pics/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ClientProfile: {self.user.username}"
    
class PostRequest(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    hunarbaaz = models.ForeignKey(Hunarbaaz, on_delete=models.CASCADE, related_name='received_requests')
    job_description = models.TextField()
    location = models.CharField(max_length=100)
    scheduled_date = models.DateField()
    is_accepted = models.BooleanField(null=True, blank=True)  # None = Pending, True = Accepted, False = Rejected
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.client.username} to {self.hunarbaaz.full_name}"
