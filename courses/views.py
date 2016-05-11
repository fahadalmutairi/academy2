from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from profiles.forms import CreateCommentForm
from courses.models import Subject, Video


class HomeView(TemplateView):
    template_name = 'home.html'




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


def video_view(request, pk):
    context = {}
    form = CreateCommentForm()
    context['comment_form'] = form
    video = Video.objects.get(pk=pk)
    context['video'] = video
    try:
        context['previous_video'] = Video.objects.get(subject__title='%s' % video.subject.title,
                                                      pk=video.pk - 1)

        Video.objects.get(pk=context['previous_video'].pk)

    except Exception, e:
        print e

    try:

        context['next_video'] = Video.objects.get(subject__title='%s' % video.subject.title,
                                                  pk=video.pk + 1)

        Video.objects.get(pk=context['next_video'].pk)

    except Exception, e:
        print e

    return render(request, 'video_detail.html', context)
