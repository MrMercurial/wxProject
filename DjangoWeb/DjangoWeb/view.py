#encoding:utf-8

from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
import datetime

def hello(request):
    try:
        ua=request.META['HTTP_USER_AGNET']
    except KeyError:
        ua = 'unknown'
    # return HttpResponse("Hello %s!!!!!"%ua)
    return HttpResponse(request.META.keys())
def login(request):
    return render_to_response('login.html')

def hello_plus(request,a,b):
    try:
        a=int(a)
        b=int(b)
    except ValueError:
        raise Http404()
    # assert False
    return HttpResponse('%d + %d = %d'%(a,b,a+b))

def home(request):
    now=datetime.datetime.now()
    # return HttpResponse(now)
    return render_to_response('base.html')

def index(request):
    return render_to_response('home.html')

def testArgs(request,secondpar):
    return HttpResponse(secondpar)