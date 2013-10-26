from django.conf.urls import patterns, url
from microblogs import views
from microblogs.views import blog_list, blog_detail

urlpatterns = patterns('',
#heres a comment

    url(r'^$', blog_list, name ='blog_list'),
    url(r'^(?P<pk>\d+)/$', blog_detail, name= 'blog_detail'),
)