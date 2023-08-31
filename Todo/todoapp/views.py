from django.shortcuts import render,redirect
from .forms import TodoForm
from .models import TodoItem

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_form.html', {'form': form})
    
def retreive(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def update(request, id):
    todo = TodoItem.objects.get(pk=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_form.html', {'form': form})

def delete(request,id):
    todo = TodoItem.objects.get(pk=id)
    todo.delete()
    return redirect('/todo_list/')