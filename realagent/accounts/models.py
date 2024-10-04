from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    ACCOUNT_TYPES = [
        ('buyer', 'Looking for Properties'),
        ('seller', 'Offering Services'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)

    def __str__(self):
        return self.user.username
