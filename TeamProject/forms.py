from django import forms
from .models import Task,User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'dateToEnd', 'status', 'user']
        widgets = {
            'dateToEnd': forms.DateInput(attrs={'type': 'date'})        }
        labels = {
            'dateToEnd': "תאריך סיום",
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1', 'password2', 'phone']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['team','role']