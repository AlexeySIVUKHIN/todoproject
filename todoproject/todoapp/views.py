from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem


def todoappView(request):
    return render(request, 'todolist.html')


def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})

def addTodoView(request):
    addAsk = request.POST['content']
    new_item = TodoListItem(content = addAsk)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    delAsk = TodoListItem.objects.get(id= i)
    delAsk.delete()
    return HttpResponseRedirect('/todoapp/')