from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

# Signal to create or update a user profile after a User is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Check if the user is a superuser
        if instance.is_superuser:
            # Assign 'seller' profile type for superusers
            UserProfile.objects.create(user=instance, profile_type=UserProfile.SELLER)
        else:
            # Default to 'buyer' profile for regular users
            UserProfile.objects.create(user=instance, profile_type=UserProfile.BUYER)
    else:
        # If user is updated, make sure profile is updated as well
        instance.userprofile.save()
