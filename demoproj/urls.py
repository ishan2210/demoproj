from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def projects(request,pk):
    return HttpResponse("Here are my projects"+ " "+str(pk))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/<str:pk>/',projects,name="projects"),
]
