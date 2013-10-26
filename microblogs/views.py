# Create your views here.
from django.shortcuts import render
from models import Post
from django.http import HttpResponse
from restless.models import serialize
from django.core.serializers.json import DjangoJSONEncoder
import json


def index(request):
    return render(request, 'index.html')


def blog_list(request, *args, **kwargs):
    post_list = (Post.objects.filter(published=True))

    # were going to serialize the data into json and return it via the url
    # first i found this package called Django restless that removes the model and the pk valies
    # but it formatted it as a unicode string
    # then i imported json and dumped that unicode string into it, along with DjangoEncoder
    # as a cls and it worked perfectly
    # the result: a perfectly json formatted string with the info you dont want shown hiddden
    # and the fields brought to the root level
    data = serialize(post_list)
    jsondata = json.dumps(data, cls=DjangoJSONEncoder)

    return HttpResponse(jsondata, mimetype='application/json')


def blog_detail(request, pk, *args, **kwargs):
    # were going to serialize the data into json and return it via the url
    # with this object using .get is not iterable because it only returns one item
    # post = Post.objects.get(pk=pk, published=True) soooo..you have to  use
    post = Post.objects.filter(pk=pk, published=True)
    data = serialize(post)
    jsondata = json.dumps(data, cls=DjangoJSONEncoder)

    return HttpResponse(jsondata, mimetype='application/json')
