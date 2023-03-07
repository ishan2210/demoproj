from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    page = 'projects'
    return render(request,'projects.html', {'page': page})
    #return HttpResponse('Here are our projects')
def project(request,pk):
    return render(request,"single-project.html")
    #return HttpResponse("Single Project"+ " "+str(pk))


