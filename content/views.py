from django.shortcuts import render
from django.http import Http404

from .models import Content

def index(request):
    content_list = Content.objects.all()
    context = {
        'content_list': content_list,
    }
    return render(request, 'content/index.html', context)


def detail(request, content_id):
    try:
        content_entry = Content.objects.get(pk=content_id)
    except:
        raise Http404('Content entry does not exist')
    return render(request, 'content/detail.html', {'content_entry': content_entry})