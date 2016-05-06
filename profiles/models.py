from __future__ import unicode_literals
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from courses.models import Level, Subject, Video

class Comment(models.Model):
    comment_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('accounts.CustomUser', null=True)
    video = models.ForeignKey('courses.Video', null=True)

    def __unicode__(self):
        return '%s' % self.author