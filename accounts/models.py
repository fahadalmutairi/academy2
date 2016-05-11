from __future__ import unicode_literals
from django.utils import timezone

from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, username, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()

        if not email:
            raise ValueError('Email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          username=username,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now,
                          **extra_fields
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        return self._create_user(email, username, password, False, False, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        return self._create_user(email, username, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', max_length=255, unique=True)
    username = models.CharField('username', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=255, blank=True, null=True)
    last_name = models.CharField('last name', max_length=255, blank=True, null=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=False)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    objects = CustomUserManager()

    fav_video = models.ManyToManyField('courses.Video')
    fav_subject = models.ManyToManyField('courses.Subject')
    fav_level = models.ManyToManyField('courses.Level')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return '/users/%s' % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
