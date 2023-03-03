from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def projects(requuest):
    return HttpResponse('Here are our projects')

def project(request):
    return HttpResponse('Here is a single project')

def demo(request):
    return HttpResponse("Here is our demo project")

def demo2(request):
    return HttpResponse("Here is our demo project")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/',projects,name="projects"),
    path('project/',project,name="project"),
    path('demo/',demo,name="demo"),
    path('demo2/',demo2,name="demo2"),

]
