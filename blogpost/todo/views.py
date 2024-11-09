from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

@login_required
def todo_list(request):
    todos = Todo.objects.filter(author=request.user)
    return render(request, 'todo/todo_list.html', {'todos': todos})

@login_required
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form})
