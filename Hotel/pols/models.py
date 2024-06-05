from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
from django_mysql.models.fields import SizedTextField


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


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)
    count_rooms = models.IntegerField()
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    CSI = models.FloatField()
    img1 = SizedTextField(size_class=3)
    img2 = SizedTextField(size_class=3)
    img3 = SizedTextField(size_class=3)
    img4 = SizedTextField(size_class=3)
    img5 = SizedTextField(size_class=3)

class Rooms(models.Model):
    title = models.CharField(max_length=100)
    beds_amount = models.IntegerField()
    bath_amount = models.IntegerField()
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    img1 = SizedTextField(size_class=3, null=True)
    img2 = SizedTextField(size_class=3, null=True)
    img3 = SizedTextField(size_class=3, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

class Card(models.Model):
    number = models.CharField(max_length=16)
    validity_period = models.DateField()
    CVV = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Booking(models.Model):
    quantity_people = models.IntegerField()
    arrival = models.DateTimeField()
    departure = models.DateTimeField()
    price_per_room = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_services = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)

class Options(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    rooms = models.ManyToManyField(Rooms)
