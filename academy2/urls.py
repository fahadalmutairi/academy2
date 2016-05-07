"""academy2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

from courses import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', 'accounts.views.sign_up'),
    url(r'^logout/$', 'accounts.views.logout_view'),
    url(r'^signin/$', 'accounts.views.login_view'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),

    url(r'^profile_page/$', 'profiles.views.profile_page'),
    url(r'^edit_profile/$', 'profiles.views.edit_profile'),

    url(r'^add_comment/(?P<pk>\d+)/$', 'profiles.views.add_comment'),

    url(r'^fav_video/(?P<pk>.+)/$', 'profiles.views.fav_video'),
    url(r'^unfav_video/(?P<pk>.+)/$', 'profiles.views.unfav_video'),

    url(r'^follow_subject/(?P<pk>.+)/$', 'profiles.views.follow_subject'),
    url(r'^unfollow_subject/(?P<pk>.+)/$', 'profiles.views.unfollow_subject'),

    url(r'^follow_level/(?P<pk>.+)/$', 'profiles.views.follow_level'),
    url(r'^unfollow_level/(?P<pk>.+)/$', 'profiles.views.unfollow_level'),


    url(r'subjects/$', views.SubjectList.as_view(), name='subject_list'),
    url(r'subjects/(?P<pk>.+)/$', views.SubjectDetail.as_view(), name='subject_detail'),
    url(r'video/(?P<pk>[0-9]+)$', 'courses.views.video_view', name='video_detail'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
