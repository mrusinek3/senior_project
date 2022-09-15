from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Sender and signal (post_save), the signal is going to be received from the receiver (create_profile function)
# All the arguments there are from the post_save signal, one is instance of user and one is created
# If the user was created then create a profile object with the user equal to the instance of the user that was created

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
