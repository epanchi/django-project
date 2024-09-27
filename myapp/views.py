from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Project, Task
# Create your views here.

def index(request):
    return render(request, "index.html")

def hello(request, username):
    print(type(username))
    return HttpResponse("Hello  %s Word s" % username)

def about(request):
    return HttpResponse("About")

def projects(request):
    projects= list(Project.objects.values())
    return render(request, "projects.html")
    # return JsonResponse(projects,safe=False)
    # return HttpResponse('projects')

def tasks(request, id):
    # task= Task.objects.get(id=id)
    task = get_object_or_404(Task,id=id)
    return HttpResponse('tasks : %s ' % task.title)