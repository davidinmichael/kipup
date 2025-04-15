from django.db import models
from django.contrib.auth.models import (
	AbstractUser, BaseUserManager,
)
from django.utils import timezone
import random

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not self.email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    
class Account(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    account_role = models.CharField(max_length=20, null=True, blank=True)
    
    objects = AccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f"{self.email} - {self.account_role}"
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f"{self.first_name}{random.randint(10, 100000)}"
        return super().save(*args, **kwargs)