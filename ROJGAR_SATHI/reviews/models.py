from django.db import models

class ContactReview(models.Model):
    USER_TYPE_CHOICES = [
        ('Hunarbaaz', 'Hunarbaaz'),
        ('Client', 'Client'),
        ('Visitor', 'Visitor'),
    ]

    QUERY_TYPE_CHOICES = [
        ('General Inquiry', 'General Inquiry'),
        ('Want to Register as Hunarbaaz', 'Want to Register as Hunarbaaz'),
        ('Work Request Support', 'Work Request Support'),
        ('Appreciation or Feedback', 'Appreciation or Feedback'),
        ('Report an Issue', 'Report an Issue'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField(blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    query_type = models.CharField(max_length=50, choices=QUERY_TYPE_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.query_type}"
