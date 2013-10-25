from django.conf.urls import patterns, include, url

#improt our settings file to serve static assets
from django.conf import settings
from microblogs.views import index
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^microblog/', include('microblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # hands off the request to the microblogs app
    url(r'^blog/', include('microblogs.urls', namespace="microblogs")),

    url(r'^$', index, name='index'),

    # url to match djangos requests for assets (js, css, img) and return them
    # change settings.Dev.... to STATIC_ROOT for production deployment (remember to run collectstatic too)
    # collectstatic pulls static files i.e. js and css and html( files that change often)
    # to the django files (files or infrastructure that will never change or rarely does)
    # so django can put them together to make the awesomeness that is a web page
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
