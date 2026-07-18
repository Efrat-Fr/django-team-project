from django.urls import path
from django.contrib.auth import views as auth_views
from .views import getAllTask,deleteTask,addUpdateTask,getTaskForTeam,findTaskNoWorker,taskAssignment,changeStatus,selectByStatus,register,home,proFile,associatedEmployee
urlpatterns = [
    path("taskList/", getAllTask, name='taskList'),
    path("addUpdateTask/update/<int:task_id>/", addUpdateTask, name='UpdateTask'),
    path("addUpdateTask/add/", addUpdateTask, name='addTask'),
    path("taskList/delete",deleteTask, name="deleteTask"),
    path("taskListByTeam/", getTaskForTeam, name='taskListByTeam'),
    path("taskNoWorker/", findTaskNoWorker, name='findTaskNoWorker'),
    path("taskAssignment/<int:task_id>/", taskAssignment, name="taskAssignment"),
    path("changeStatus/<int:task_id>/",changeStatus, name="changeStatus"),
    path("selectByStatus/",selectByStatus ,name="selectByStatus"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'),name='logout'),
    path('register/',register, name='register'),
    path('profile/',proFile,name='profile'),
    path('selectByUser/', associatedEmployee, name='selectByUser'),
    path('',home,name='home')
]