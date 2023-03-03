from django.shortcuts import render
from django.http import HttpResponse

def projects(request,pk):
    return HttpResponse('Here are our projects'+ " "+ str(pk))
def project(request,pk):
    return HttpResponse("Single Project"+ " "+str(pk))
