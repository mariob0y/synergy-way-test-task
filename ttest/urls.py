"""ttest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from users.views import user_show, user_create, user_delete, user_edit, user_list, group_list, group_create, group_edit, group_delete, error_page, api_user_create, api_group_create
from django.shortcuts import redirect

#react realted
from django.views.generic import TemplateView

urlpatterns = [
    path('', lambda req: redirect('users/')),
    path('api/users/', api_user_create.as_view() ),
    path('api/groups/', api_group_create.as_view() ),
    path('groups/', group_list),
    path('groups/create', group_create.as_view(), name='groupcreate'),
    path('groups/<int:id>/edit/', group_edit.as_view(), name='groupedit'),
    path('groups/<int:id>/delete/', group_delete.as_view()),
    path('admin/', admin.site.urls),
    path('users/<int:id>/delete/', user_delete.as_view()),
    path('users/create/', user_create.as_view(), name='create'),
    path('users/', user_list),
    path('users/<int:id>/edit/', user_edit.as_view(), name='edit'),
    path('error/', error_page)
]
