from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ToDoForm

from .models import ToDo

# Create your views here.

def todoList(request):
    todos = ToDo.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'todos': todos})

def todoView(request, id):
    todo = get_object_or_404(ToDo, pk=id)
    return render(request, 'tasks/task.html', {'todo': todo})

def newTask(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        
        if form.is_valid():
            todo = form.save(commit=False)
            todo.done = 'doing'
            todo.user = request.user
            todo.save()
            return redirect('/')
    else:
        form = ToDoForm()
        return render(request, 'tasks/addtask.html', {'form': form})


def editTask(request, id):
    todo = get_object_or_404(ToDo, pk=id)
    form = ToDoForm(instance=todo)

    if(request.method == 'POST'):
        form = ToDoForm(request.POST, instance=todo)

        if(form.is_valid()):
            todo.save()
            return redirect('/')
        else:
           return render(request, 'tasks/edittask.html', {'form': form, 'todo': todo}) 
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'todo': todo})

def helloWorld(request):
    return HttpResponse('Hello World!')
