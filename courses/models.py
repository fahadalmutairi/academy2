from django.utils import timezone

from django.db import models
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from accounts.models import CustomUser

# Create your models here.


class Level(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return '%s' % self.title


class Subject(models.Model):
    level = models.ForeignKey('courses.Level', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return '%s' % self.title


class Video(models.Model):
    subject = models.ForeignKey('courses.Subject', max_length=255)
    video_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    video_order = models.IntegerField(null=True, blank=True)
    available = models.BooleanField(default=True)
    date_published = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return '%s - %s - %s' % (self.subject.title, self.video_order, self.title)
