from django.contrib import admin

# Register your models here.
from profiles.models import Comment

admin.site.register(Comment)