from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects
# Create your views here.


def projects(request):
    page = "projects"
    number = 11

    context = {'page': page, "number" : number}
    return render(request, 'projects/projects.html', context)




def project(request, pk):
    page = "single project"
    return render(request, 'projects/single-project.html', {"page": page})





def fetch_projecs(request):
    data = Projects.objects.all()

    
