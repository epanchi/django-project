from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Project, Task
# Create your views here.

def index(request):
    title='Welcome to django'
    return render(request, "index.html",{
        'title':title
    })


def hello(request, username):
    print(type(username))
    return HttpResponse("Hello  %s Word s" % username)

def about(request):
    username='edison'
    return render(request, "about.html",{
        'username':username
    })

def projects(request):
   ## projects= list(Project.objects.values())
    projects=Project.objects.all()
    return render(request, "projects.html",{
        'projects':projects
    })
    # return JsonResponse(projects,safe=False)
    # return HttpResponse('projects')

def tasks(request):
    # task= Task.objects.get(id=id)
    #task = get_object_or_404(Task,id=id)
    tasks=Task.objects.all()
    return render(request, "tasks.html",{
        'tasks':tasks
    })
    ##return HttpResponse('tasks : %s ' % task.title)   