from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import EmailValidator, ValidationError

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True)
    image = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    dob = models.DateField(max_length=8)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)

class UserAccount(models.Model):
    username = models.CharField(max_length=1000, unique=True)
    password = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
