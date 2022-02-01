from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    profile_image =models.URLField(null=True)
    otp = models.CharField(null=True, max_length=6)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username} {self.email}"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


