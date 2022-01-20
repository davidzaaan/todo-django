from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('add-task/', views.add_task, name='add'),
    path('edit-task/<str:pk>', views.edit_task, name='edit'),
    path('home/', views.home, name='home'),
]