"""
URL configuration for RaiseTogether project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import all_project, upload_multi_picture, project_detail, add_rating,create_project,deleteProject,editForm


urlpatterns = [
    path("", all_project, name="all_project"),
    path('project_detail/<int:project_id>/', project_detail, name='project_detail'),
    path('upload/<int:project_id>/', upload_multi_picture, name='upload_multi_picture'),
    path('add_rating/<int:project_id>/', add_rating, name='add_rating'),
    path('forms/create',create_project, name='projects.create' ),
    path('forms/edit/<int:project_id>',editForm, name='projects.edit' ),
    path('<int:id>',deleteProject,name='project.delete'),
]
