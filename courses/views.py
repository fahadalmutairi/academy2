from django.shortcuts import render
from django.views.generic import ListView, DetailView
from courses.models import Subject, Video


class SubjectList(ListView):
    model = Subject
    template_name = 'subjects.html'
    context_object_name = 'subjects'

class SubjectDetail(DetailView):
    model = Subject
    template_name = 'subject_detail.html'
    context_object_name = 'subject'

class VideoList(ListView):
    model = Video
    template_name = 'videos.html'
    context_object_name = 'videos'
