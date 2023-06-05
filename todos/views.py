from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    if request.method=='POST':
        task=request.POST["task"]
        task=Task.objects.create(task=task)
    return redirect('home')
