from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from datetime import date
from crowdfunder.models import *
