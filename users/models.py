from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  password = models.CharField(max_length=30, validators=[MinLengthValidator(8, 'Your password should have at least 8 characters')])
  is_Admin = models.BooleanField()