from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.api_user_create.as_view() ),
    path('api/groups/', views.api_group_create.as_view() )
]