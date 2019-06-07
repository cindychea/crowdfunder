from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import date
from crowdfunder.models import Project, Reward, Backing 
from crowdfunder.forms import ProjectForm, LoginForm, SignUpForm


def root(request):
    return HttpResponseRedirect('/home')


def home_page(request):
    context = {
        'title': 'Crowdfunder',
        'projects': Project.objects.all(),
    }
    response = render(request, 'home.html', context)
    return HttpResponse(response)


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


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('username', 'Login Failed')
    else:
        form=LoginForm()

    context = {'form': form, 'title': 'Login'}
    return render(request, 'login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form': form, 'title': 'Sign Up'}
    return render(request, 'signup.html', context)

@login_required
def profile_view(request, id):
    user = User.objects.get(pk=id)
    context = {
        'user': user
        }
    return render(request, 'profile.html', context)