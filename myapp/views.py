from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("index")
def hello(request, username):
    print(type(username))
    return HttpResponse("Hello  %s Word s" % username)

def about(request):
    return HttpResponse("About")