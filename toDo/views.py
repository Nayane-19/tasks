from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ToDoForm
from django.contrib import messages
from django.core.paginator import Paginator

from .models import ToDo

# Create your views here.
@login_required
def todoList(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        todos = ToDo.objects.filter(title__icontains=search, user=request.user)
    
    elif filter:
        todos = ToDo.objects.filter(done=filter, user=request.user)

    else:
        todos_list = ToDo.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(todos_list, 5)

        page = request.GET.get('page')

        todos = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'todos': todos})

@login_required
def todoView(request, id):
    todo = get_object_or_404(ToDo, pk=id)
    return render(request, 'tasks/task.html', {'todo': todo})

@login_required
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

@login_required
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

@login_required
def deleteTask(request, id):
    todo = get_object_or_404(ToDo, pk=id)
    todo.delete()

    messages.info(request, 'Tarefa deletada com sucesso')

    return redirect('/')

@login_required
def changeStatus(request, id):
    todo = get_object_or_404(ToDo, pk=id)

    if(todo.done == 'doing'):
        todo.done = 'done'
    else:
        todo.done = 'doing'

    todo.save()

    return redirect('/')

def helloWorld(request):
    return HttpResponse('Hello World!')
