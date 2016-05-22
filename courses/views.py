from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView, TemplateView
from profiles.forms import CreateCommentForm
from courses.models import Subject, Video
from django.db.models import Q


class PrivacyPolicy(TemplateView):
    template_name = 'privacy_policy.html'


class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = {}
        recent_videos = Video.objects.all()
        updated_subjects = Subject.objects.all()
        context['recent_videos'] = list(recent_videos)[-3:]
        context['updated_subjects'] = list(updated_subjects)[-3:]
        return context




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

    def get_queryset(self):
        print self.request
        try:
            title = self.kwargs['title']
            print title
        except:
            name = ''
            print 'no name'
        if (title != ''):
            object_list = self.model.objects.filter(title__icontains = title)
        else:
            object_list = self.model.objects.all()
        return object_list


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



