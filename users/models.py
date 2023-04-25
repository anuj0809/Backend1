from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser,PermissionsMixin):
    email             = models.EmailField(_('email address'), unique=True,db_index=True)
    is_staff          = models.BooleanField(_('is_staff'),default=False)
    is_superuser      = models.BooleanField(_('is_superuser'),default=False)
    is_active         = models.BooleanField(_('is_active'),default=True)
    date_joined       = models.DateTimeField(_('date_joined'),default=timezone.now)

    USERNAME_FIELD    = 'email'
    REQUIRED_FIELDS   = []

    objects           = UserManager()

    def __str__(self):
        return self.email