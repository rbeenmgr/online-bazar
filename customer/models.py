from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    CUSTOMER = 1
    VENDOR = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (CUSTOMER, 'customer'),
        (VENDOR, 'vendor'),
        (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()



class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    roles = models.ManyToManyField(Role)
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=255, default='')
    address = models.CharField(max_length=100, default='')
    telephone = models.CharField(max_length=100, default='')
   
    def __str__(self):
        return self.user.username

    