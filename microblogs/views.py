# Create your views here.
from django.shortcuts import render, get_object_or_404
from models import Post
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


#def index(request):
#    return render(request, 'index.html')


def blog_list(request, *args, **kwargs):
    post_list = Post.objects.filter(published=True)
    template_name = 'post_list.html'

    context = {
        "post_list": post_list
    }

    return render(request, template_name, context)


def blog_detail(request, pk, *args, **kwargs):
    post = Post.objects.get(pk=pk, published=True)
    template_name = 'post_detail.html'

    context = {
        "post": post
    }

    return render(request, template_name, context)