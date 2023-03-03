from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def projects(request):
    return HttpResponse("Here are our projects")

def ishan(request):
    return HttpResponse("Ishan Kansara King of mirzapur")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/',projects,name="projects"),
    path('ishan/',ishan,name="ishan"),

]
