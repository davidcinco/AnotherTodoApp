from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from django.shortcuts import render

from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()

    context = {"message": "hello world", "tasks": todos}
    return render(request, 'todo/index/index.html', context)

def create(request):
    return HttpResponse("create views from todo")
        
def update(request, id):
    return HttpResponse(f"update views from todo - {id}")

def delete(request, id):
    return HttpResponse(f"delete views from todo - {id}")

