from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, null=True, default="No Address Avaliable")
    phone = models.CharField(max_length=30, null=True, default="No Phone Number Avaliable")

    def __str__(self):
        return f'{self.user.username} Profile'