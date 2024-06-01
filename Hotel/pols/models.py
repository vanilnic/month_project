from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid


# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = models.UUIDField(unique=True, default=uuid.uuid4)
    email = models.EmailField(unique=True, verbose_name='Почта', null=False, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()
