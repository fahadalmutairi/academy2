from __future__ import unicode_literals

from django.http import HttpResponseRedirect, Http404
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from courses.models import Level, Video, Subject
from profiles.forms import CreateCommentForm, EditProfileForm
from . import forms
from . import models
from accounts.models import CustomUser


# add feedback messages

def add_comment(request, pk):
    context = {}
    video = Video.objects.get(pk=pk)

    if request.method == 'POST':
        form = CreateCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.video = video
            comment.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def fav_video(request, pk):
    user = CustomUser.objects.get(pk=request.user.pk)
    video = Video.objects.get(pk=pk)

    user.fav_video.add(video)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unfav_video(request, pk):
    user = CustomUser.objects.get(pk=request.user.pk)
    video = Video.objects.get(pk=pk)

    user.fav_video.remove(video)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def follow_level(request, pk):
    user = CustomUser.objects.get(pk=request.user.pk)
    level = Level.objects.get(pk=pk)
    user.fav_Level.add(level)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unfollow_level(request, pk):
    user = CustomUser.objects.get(pk=request.user.pk)
    level = Level.objects.get(pk=pk)
    user.fav_Level.remove(level)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def follow_subject(request, pk):
    user = CustomUser.objects.get(pk=request.user.pk)
    subject = Subject.objects.get(pk=pk)
    user.fav_subject.add(subject)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unfollow_subject(request, pk):
    user = CustomUser.objects.get(pk=request.user.pk)
    subject = Subject.objects.get(pk=pk)
    user.fav_subject.remove(subject)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def profile_page(request):
    context = {}

    print request.user
    print request.user.pk
    try:
        context['user'] = CustomUser.objects.get(pk=request.user.pk)
    except Exception, e:
        raise Http404('404')
    return render(request, 'profile_page.html', context)


def edit_profile(request):
    context = {}
    try:
        user = CustomUser.objects.get(pk=request.user.pk)
    except Exception, e:
        raise Http404('404')

    form = EditProfileForm(request.POST or None, instance=user)

    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/profile/')
    else:
        print form.errors
    return render(request, 'edit_profile.html', context)
