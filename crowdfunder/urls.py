"""crowdfunder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crowdfunder import views

urlpatterns = [
    path('', views.root),
    path('admin/', admin.site.urls),
    path('home/', views.home_page, name='home'),
    path('project/<int:id>', views.display_project, name='display_project'),
    path('project/<int:id>/add_reward', views.add_reward, name='add_reward'),
    path('project/<int:id>/contrib/<int:reward_id>/', views.back_project, name='back_project'),
    path('project/create', views.create_project, name='create_project'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/<int:id>', views.profile_view, name='profile'),
]
