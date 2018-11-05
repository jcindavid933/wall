from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^travels/$', views.success),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^reset$', views.reset)
]
