from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


app_name = 'accounts'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', 'accounts.views.sign_up', name='sign_up'),
    url(r'^logout/$', 'accounts.views.logout_view', name='sign_out'),
    url(r'^signin/$', 'accounts.views.login_view', name='sign_in'),

]
