from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import EmailValidator, ValidationError

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=32)
    image = models.CharField(max_length=200)
    dob = models.DateField(max_length=8)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    interest = ArrayField(models.CharField(max_length=25), blank=True)
    attended = ArrayField(models.CharField(max_length=50), blank=True)
    wishlist = ArrayField(models.CharField(max_length=50), blank=True)
