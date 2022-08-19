from struct import pack
from zlib import DEF_BUF_SIZE
from django.shortcuts import render, redirect
from .models import Task    

# Create your views here.
def list_tasks(request):

    tasks = Task.objects.all()

    return render(request,'list_tasks.html', {'tasks': tasks})

def create_task(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save() 
    
    return redirect('/tasks/')

# Delete tasks
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()

    return redirect('/tasks/')