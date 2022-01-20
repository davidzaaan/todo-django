from django.shortcuts import render, redirect
from django.http import HttpResponse

# model importing
from todo.models import Task, UserTaskProfile


# rest_framework handler
from rest_framework.decorators import api_view
from rest_framework.response import Response

# rest serializers
from .serializers import TaskSerializer


@api_view(['GET'])
def index(request):
    api_urls = {
        'Tasks List': '/task-list/',
        'Task Details': '/task-detail/<str:pk>/',
        'Create Task': '/task-create/',
        'Update Task': '/task-update/<str:pk>/',
        'Delete Task': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    # TaskSerializer will handle all the serialize data...
    # ...and we need to store it in a variable
    serializer = TaskSerializer(tasks, many=True) 
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task) 
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    try:
        user_task_profile = UserTaskProfile.objects.get(user=request.user)
    except:
        return Response({ 'error': 'No user found'})

    task_name = request.data['task_name']
    task_description = request.data['task_description']
    
    new_task = Task.objects.create(owner=user_task_profile, task_name=task_name, task_description=task_description)

    serializer = TaskSerializer(new_task)

    return Response(serializer.data)


@api_view(['PATCH'])
def task_update(request, pk):
    try:
       task = Task.objects.get(id=pk)
    except:
        return Response({ 'error': 'No user found'})


    if 'task_description' in request.data:
        task.task_description = request.data['task_description']
    elif 'task_name' in request.data:
        task.task_name = request.data['task_name']
    elif 'completed' in request.data:
        task.completed = request.data['completed']
    else:
        pass

    task.save()

    serializer = TaskSerializer(task)

    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except:
        return Response({ 'error': 'Could not find task'})

    task.delete()

    return Response({'success': 'Task deleted successfully'})


@api_view(['PATCH'])
def task_complete(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except:
        return Response({ 'error': 'Could not find task'})

    task.completed = True
    task.save()

    serializer = TaskSerializer(task)
    return Response(serializer.data)

""" TO DO 
    2. Wire up the JWT authentication
    3. Allow CORS from a FrontEnd app
"""