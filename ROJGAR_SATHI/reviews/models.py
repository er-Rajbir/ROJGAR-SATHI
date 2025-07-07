from django.db import models
from django.db import models
from django.contrib.auth.models import User
from hunarbaaz.models import Hunarbaaz
from client.models import ClientProfile

class HunarbaazReview(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    hunarbaaz = models.ForeignKey(Hunarbaaz, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    review_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.hunarbaaz.full_name} by {self.reviewer.username}"

class ClientReview(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    review_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.client.full_name} by {self.reviewer.username}"

# Create your models here.
