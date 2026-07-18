from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm,RegisterForm,ProfileForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


@login_required
def getAllTask(request):
    tasks = Task.objects.all()
    return render(request, 'allTask.html', {
        'tasks': tasks
    })

def addUpdateTask(request, task_id=None):
    if task_id:
        task = get_object_or_404(Task, id=task_id)
        current_status = task.status
    else:
        task = None
        current_status = ''
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('taskList')
    else:
        form = TaskForm(instance=task)
    return render(request, 'addTask.html', {'form': form, 'task': task, 'current_status': current_status})


def deleteTask(request):
    if request.method == "POST":
        Task.objects.filter(user__isnull=True).delete()
    return redirect('taskList')

@login_required
def getTaskForTeam(request):
    if not request.user.team:
        tasks = Task.objects.none()
    else:
        tasks = Task.objects.filter(user__team=request.user.team)

    return render(request, 'getTaskByTeam.html', {
        'tasks': tasks,'user':request.user
    })

@login_required
def findTaskNoWorker(request):
    tasks = Task.objects.filter(user__isnull=True)
    return render(request, 'taskAssignmemt.html', {
        'tasks': tasks
    })

@login_required
def taskAssignment(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.status = "in Progress"
        task.user = request.user
        task.save()
    return redirect("findTaskNoWorker")

@login_required
def changeStatus(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.status = request.POST['status']
        task.save()
    return redirect("taskListByTeam")


def selectByStatus(request):
    source=request.GET.get('from')
    statusSelect=request.GET.get('status','')
    if statusSelect:
        tasks = Task.objects.filter(status=statusSelect)
    else:
        tasks=Task.objects.all()
    if source=='allTask':
        return render(request, 'allTask.html', {
            'tasks': tasks,
            'statusSelect':statusSelect,
        })
    elif source=='byTeam':
        return render(request, 'getTaskByTeam.html', {
            'tasks': tasks,
            'statusSelect': statusSelect,
        })
    return render(request, 'home.html', {
        'tasks': tasks,
        'statusSelect': statusSelect,
    })

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'register.html', {
                'form':form
            })
    else:
        form = RegisterForm()
    return render(request, 'register.html',{
        'form':form
    })

def home(request):
    return  render(request,'home.html')

def proFile(request):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'profile.html', {
        'form': form
    })

def associatedEmployee(request):
    source = request.GET.get('from')
    user=request.user
    tasks=Task.objects.filter(user=user)
    if source=='allTask':
        return render(request, 'allTask.html', {
            'tasks': tasks,
        })
    elif source=='byTeam':
        return render(request, 'getTaskByTeam.html', {
            'tasks': tasks,
        })
    return render(request, 'home.html', {
        'tasks': tasks,
    })