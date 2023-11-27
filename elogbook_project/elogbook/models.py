from django.db import models

# Create your models here.
# models.py

from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
    name = models.CharField(max_length=255)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    # Add other fields as needed

class Week(models.Model):
    number = models.PositiveIntegerField()

class Day(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    date = models.DateField()
    is_holiday = models.BooleanField(default=False)

class Activity(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_assessed = models.BooleanField(default=False)
