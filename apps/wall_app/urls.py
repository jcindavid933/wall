from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^message$', views.message),
    url(r'^comment$', views.comment),
    url(r'^delete$', views.delete_message)
]
