from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    if request.method == 'POST':
        text = request.POST.get("text").strip()
        if text:
            Todo.objects.create(text=text)
        return redirect('/')

    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)


def deleteTodo(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('/')


def about(request):
    return render(request, 'todo/about.html')