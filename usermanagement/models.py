from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        _('Username'), max_length=250, blank=False, unique=True, null=False)

    fullname = models.CharField(max_length=250, blank=False, null=False)

    email = models.EmailField(
        _('Email address'), unique=True, blank=False, null=False)

    phonenumber = models.CharField(
        _('Phone number'), unique=True, blank=False, null=False)

    profile_img = models.ImageField(
        _('Profile Image'), upload_to='profile_images/', blank=True, null=True)

    edited_on = models.DateField(_('Edited on'), auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'phonenumber']

    def __str__(self):
        return f"{self.email}"
