from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms
from .models import Task

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name'
        }

        def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['password1'].widget.attrs.update({'type': 'password'})
            self.fields['password2'].widget.attrs.update({'type': 'password'})
            for field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control'})
                


class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_description']
        
        def __init__(self, *args, **kwargs):
            super(AddTaskForm, self).__init__(*args, **kwargs)
            
            
            for field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control'})


class EditTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_description']
        labels = {
            'task_name': 'new task name (optional)',
            'task_description': 'task desc (optional)'
        }
        def __init__(self, *args, **kwargs):
            super(EditTaskForm, self).__init__(*args, **kwargs)
            
            for field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control'})
