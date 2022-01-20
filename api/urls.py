from http.client import HTTPResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index_api"),
    path('task-list/', views.task_list, name="task_list"),
    path('task-detail/<str:pk>/', views.task_detail, name="task_detail"),
    path('task-create/', views.task_create, name="task_create"),
    path('task-update/<str:pk>/', views.task_update, name="task_update"),
    path('task-delete/<str:pk>/', views.task_delete, name="task_delete"),
    path('task-complete/<str:pk>/', views.task_complete, name="task_complete"),
]