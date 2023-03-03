from django.shortcuts import render
from django.http import HttpResponse

def projects(request,pk):
    return render(request,'projects.html')
    #return HttpResponse('Here are our projects'+ " "+ str(pk))
def project(request,pk):
    return render(request,"single-project.html")
    #return HttpResponse("Single Project"+ " "+str(pk))


