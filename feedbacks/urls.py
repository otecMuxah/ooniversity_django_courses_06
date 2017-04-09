from django.conf.urls import include, url

from feedbacks import views


urlpatterns = [
    url(r'^$', views.FeedbackView.as_view(), name='feedback'),
]