from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Bb


def index(request):
    bbs = Bb.objects.all()
    context = {'bbs': bbs}

    return render(request, 'bboard/index.html', context=context)

# def index(request):
#     s = 'Список объявлений\r\n\r\n\r\n'
#     for bb in Bb.objects.all().order_by('-published'):
#         s += bb.title + '\r\n' + bb.content + '\r\n'
#
#     return HttpResponse(s, content_type='text/plain; charset=utf-8')
