from django.shortcuts import render
from django_project.models import Django_Project

# Create your views here.


def project_index(request):
    projects = Django_Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Django_Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)