from django.db import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=200)
    manager=models.OneToOneField("User",on_delete=models.CASCADE, related_name='managed_teams')
    def __str__(self):
        return self.name
class User(AbstractUser):
    phone = models.CharField(max_length=11)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=10, choices=[('manager', 'Manager'), ('employee', 'Employee')], default="employee")

    def __str__(self):
        return self.username

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    dateToEnd = models.DateField()
    STATUS_CHOICES=[
        ("new", "New"),
        ("inProgress", "In Progress"),
        ("done", "Done"),
    ]
    status=models.CharField(max_length=15,choices=STATUS_CHOICES,default="new")
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
