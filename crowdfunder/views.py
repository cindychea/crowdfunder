from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from datetime import date
from crowdfunder.models import Project, Reward, Backing 
from crowdfunder.forms import ProjectForm


def root(request):
    return HttpResponseRedirect('/home')


def home_page(request):
    projects = Project.objects.all()
    return HttpResponse(render(request, 'index.html', {'projects': projects}))

def display_project(request, id):
    project = Project.objects.get(pk=id)
    context = {'project': project}
    return render(request, 'display_project.html', context)

def create_project(request):
    project_form = ProjectForm()
    if request == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect(reverse('display_project'))
    else:
        context = {'project_form': project_form, 'title': 'Create A Project'}
    return render(request, 'create_project.html', context)
