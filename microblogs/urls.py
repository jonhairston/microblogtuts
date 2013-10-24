from django.conf.urls import patterns, url
from microblogs import views

urlpatterns = patterns('',
#heres a comment

    url(r'^$', views.index, name ='index')
)