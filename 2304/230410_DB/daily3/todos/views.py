from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todos/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()

    context = {'form': form}
    return render(request, 'todos/create.html', context)

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == todo.author:
            todo.delete()
            return redirect('todos:index')
    return redirect('todos:index')

def change(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user == todo.author:
        if request.method == 'POST':
            if todo.completed == True:
                todo.completed = False
            else:
                todo.completed = True
            todo.save()
        return redirect('todos:index')
