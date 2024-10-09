from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.template import loader
from django.shortcuts import render

from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {"tasks": todos}
    return render(request, 'todo/index/index.html', context)

def create(request):
    form = TodoForm
    if request.method == "POST":            
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect("todo:index")
    
        
def update(request, id):
    return HttpResponse(f"update views from todo - {id}")

def delete(request, id):
    task = Todo.objects.get(pk=id)
    if task.DoesNotExist():
        task.delete()
        
    return redirect("todo:index")

