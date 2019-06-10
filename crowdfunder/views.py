from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from datetime import date
from crowdfunder.models import Project, Reward, Contribution
from crowdfunder.forms import ProjectForm, LoginForm, SignUpForm, RewardForm



def root(request):
    return HttpResponseRedirect('/home')


def home_page(request):
    context = {
        'title': 'Crowdfunder',
        'projects': Project.objects.all(),
    }
    response = render(request, 'home.html', context)
    return HttpResponse(response)


def display_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    projects = Project.objects.filter(owner=project.owner)
    form = RewardForm()
    context = {
        'title': project.title,
        'project': project,
        'projects': projects,
        'form':form
        }
    return render(request, 'display_project.html', context)

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.instance
            project.owner = request.user
            project.save()
            return redirect('display_project', project_id=project.id)
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {
        'project_form': form,
        'title': 'Create A Project'
    })

@login_required
def add_reward(request, project_id):
    if request.method == 'POST':
        project = Project.objects.get(pk=project_id)
        form = RewardForm(request.POST)
        if form.is_valid():
            reward = form.instance
            reward.project = project
            reward.save()
            return redirect('display_project', project_id=project.pk)
    else:
        form = RewardForm()

    return render(request, 'display_project.html', {
        'project_form': form
    })

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

@login_required
@require_http_methods(["POST"])
def back_project(request, reward_id, project_id):
    reward = Reward.objects.get(pk=reward_id)
    project = Project.objects.get(pk=project_id)

    contribution = Contribution()
    contribution.reward = reward
    contribution.project = project
    contribution.user = request.user

    if contribution.save():
        return redirect('display_project', project_id=project.id)
    else:
        # TODO: Errors
        return redirect('display_project', project_id=project.id)