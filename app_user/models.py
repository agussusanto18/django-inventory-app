from django.db import models
from django.contrib.auth.models import User
from constants.choices import Gender

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/user', blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MALE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    