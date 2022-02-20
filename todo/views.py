from django.shortcuts import render, redirect
from .models import UserTaskProfile, Task
from .forms import RegisterForm, AddTaskForm, EditTaskForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .greeting import get_greeting_time, get_location



def login_user(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, 'User does not exist')
            return render(request, 'login.html')

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
            task_name = request.POST['task_name'].strip()
            task_description = request.POST['task_description'].strip()

            if len(task_name) != 0:
                task.task_name = task_name
            else:
                pass

            if len(task_description) != 0:
                task.task_description = task_description
            else:
                pass
                
            task.save()
            messages.success(request, f"Task updated")
            return redirect('home')
    
    return render(request, 'edit.html', {
        'form': form,
        'task': task
    })

