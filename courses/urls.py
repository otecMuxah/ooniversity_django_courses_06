from django.conf.urls import include, url

from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^(?P<course_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<course_id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<course_id>\d+)/$', views.remove, name='remove'),
    url(r'^(?P<course_id>[0-9]+)/add_lesson/$', views.add_lesson, name='add-lesson'),
]