from django.shortcuts import render, redirect
from .models import UserTaskProfile, Task
from .forms import RegisterForm, AddTaskForm, EditTaskForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .greeting import get_greeting_time, get_location
import geocoder



def login_user(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']
        print('username:', username, 'password:', password)
        
        try:
            user = User.objects.get(username=username)
        except:
            print('no existe .l.')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Username OR password is incorrect') # messages display

    return render(request, 'login.html')

@login_required(login_url='login')
def logout_user(request):
    """ Popping up the user session"""
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')


@login_required(login_url='login')
def home(request):
    profile = UserTaskProfile.objects.get(user=request.user)

    location  = get_location()
    message = get_greeting_time(location)
    
    return render(request, 'home.html', {
        'user': profile,
        'tasks': profile.task_set.all(),
        'message': message
    })


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        print('so far so good')
        form = RegisterForm(request.POST)

        if form.is_valid():
            print('still good') 
            user = form.save(commit=False) # form makes the instance of a model
            user.username = user.username.lower() # set the username of the User model
            user.save()
            messages.success(request, 'Registered successfully!')
            
            # login(request, user)
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Try again.')

    

    return render(request, 'register.html', {
        'form': form
    })

@login_required(login_url='login')
def add_task(request):
    form = AddTaskForm()
    user = UserTaskProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = user
            task.save()
            messages.success(request, 'Task added!')
            return redirect('home')
    return render(request, 'add-task.html', {
        'form': form
    })

@login_required(login_url='login')
def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    form = EditTaskForm(instance=task)

    if request.method == 'POST':
        form = EditTaskForm(request.POST)

        if form.is_valid():
            if 'task_name' in request.POST:
                task.task_name = request.POST['task_name']
                print(request.POST['task_name'])
            if 'task_description' in request.POST:
                task.task_description = request.POST['task_description']
                print(request.POST['task_description'])
                
            task.save()
            messages.success(request, f"Task with id: {task.id} has been updated")
            return redirect('home')
    
    return render(request, 'edit.html', {
        'form': form,
        'task': task
    })

