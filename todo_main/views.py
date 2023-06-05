from django.shortcuts import render
from todos.models import Task

def home(request):
    tasks=Task.objects.filter(is_completed=False).order_by("-update_at")
    context={
        "tasks":tasks
    }
    #print(tasks)
    return render(request,"home.html",context)

