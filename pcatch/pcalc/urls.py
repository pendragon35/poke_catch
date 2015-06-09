from django.conf.urls import url
from . import views

urlpatterns = [
  # index
  url(r'^$', views.index, name = 'index'),
  # resulting catch rate
  url(r'^catch_rate/$', views.catch_rate, name = "catch_rate"),
]