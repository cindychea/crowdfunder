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
from django.urls import path, include
from crowdfunder import views, settings
from django.conf.urls import url
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('', views.root),
    path('admin/', admin.site.urls),
    path('home/', views.home_page, name='home'),
    path('project/<int:project_id>', views.display_project, name='display_project'),
    path('project/<int:project_id>/delete', views.delete_project, name='delete_project'),
    path('project/<int:project_id>/add_reward', views.add_reward, name='add_reward'),
    path('project/<int:project_id>/contrib/<int:reward_id>/', views.back_project, name='back_project'),
    path('project/create', views.create_project, name='create_project'),
    path('stats/', views.stats, name='stats'),
    path('success/', views.success, name='success'),
    path('unsuccessful/', views.unsuccessful, name='unsuccessful'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/<int:id>/', views.profile_view, name='profile'),
    path('categories/<int:category_id>/', views.categories_view, name='categories'),
    path('search/', views.search, name='search'),
]

urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})]