from django.shortcuts import render
from django.http import HttpResponse

projectsList = [

    {
      'id': '1',
      'title': 'Ecommerce Website',
      'description': 'Fully functional ecommerce website'
    },
    {
       'id': '2',
       'title': 'Portfolio Website',
       'description': 'This was a project where we built our portfolio'
    },
    {
       'id': '3',
       'title': 'Socialmedia website',
       'description': 'This is our social media page'
    },

]

def projects(request):
    page = 'projects'
    number=10
    context={'page': page,'number':number,'projects':projectsList}
    return render(request,'projects.html',context)
    #return HttpResponse('Here are our projects')
def project(request,pk):
    return render(request,"single-project.html")
    #return HttpResponse("Single Project"+ " "+str(pk))


