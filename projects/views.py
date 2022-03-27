from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This was a project where I built out my portfolio'
    },
    {
         'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project I am still working on'
    }
]

def projects(request):
    # page = 'projects'
    # number = 10
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    # return HttpResponse('SINGLE PROJECT ' + str(pk))
    project_obj = Project.objects.get(id=pk)
    # tags = project_obj.tags.all()
    print("project_obj: ", project_obj)
    return render(request, 'projects/single-project.html', {'project': project_obj})

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html',context)
