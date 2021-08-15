from django.http.response import Http404
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.context import Context
from django.views import generic
from .models import Todolist, Todoitem

class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todolists'

    def get_queryset(self):
        return Todolist.objects.all()

def detail(request, list_id):
    try:
        todolist = Todolist.objects.get(id=list_id)
    except Todolist.DoesNotExist:
        raise Http404("this list does not exist")
    items_list = Todoitem.objects.filter(todo_list = todolist)
    context = {
        'todolist' : todolist,
        'items_list' : items_list
        }
    return render(request, 'todo/detail.html',context)

def create(request):
    if request.method == 'GET':
        return render(request, 'todo/createlist.html')
    
    name = request.POST["name"]
    res = Todolist.objects.filter(list_name=name)
    if len(res)>0:
        messages.error(request,'List already present')
        return render(request, 'todo/createlist.html')
    else:
        Todolist.objects.create(list_name=name)
        lists = Todolist.objects.all()
        context = {
            'todolists' : lists
        }
        return render(request, 'todo/index.html', context )

def delete(request,list_id):
    try:
        todolist = Todolist.objects.get(id=list_id)
        res = Todolist.objects.filter(id=list_id)
    except Todolist.DoesNotExist:
        raise Http404("this list does not exist")
    res.delete()
    lists = Todolist.objects.all()
    context = {
        'todolists' : lists
    }
    return render(request, 'todo/index.html', context )

def update(request,list_id):
    try:
        todolist = Todolist.objects.get(id=list_id)
        res = Todolist.objects.filter(id=list_id)
    except Todolist.DoesNotExist:
        raise Http404("this list does not exist")
        
    if request.method == 'GET':
        context = {
        'todolist' : todolist,
    }
        return render(request, 'todo/updatelist.html',context)
    
    name = request.POST["name"]
    try:
        check = Todolist.objects.get(list_name=name)
        messages.error(request,'List already present')
        context = {
            'todolist' : todolist,
        }
        return render(request, 'todo/updatelist.html',context)
    except:
        res.update(list_name=name)
        lists = Todolist.objects.all()
        context = {
            'todolists' : lists
        }
        return render(request, 'todo/index.html', context )


def create_item(request, list_id):
    todolist = Todolist.objects.get(id=list_id)
    if request.method == 'GET':
        context = {
        'todolist' : todolist
        }
        return render(request, 'todo/createitem.html',context)

    todolist = Todolist.objects.get(id=list_id)
    title1 = request.POST["title"]
    date = request.POST["duedate"]
    res = Todoitem.objects.filter(title=title1,todo_list=todolist)
    if len(res)>0:
        messages.error(request,'Item already present')
        context = {
        'todolist' : todolist
        }
        return render(request, 'todo/createitem.html',context)
    else: 
        Todoitem.objects.create(title=title1,checked=False,due_date=date,todo_list=todolist)
        lists = Todolist.objects.all()
        context = {
            'todolists' : lists
        }
        return render(request, 'todo/index.html', context )

def update_item(request,list_id,item_id):
    try:
        todolist = Todolist.objects.get(id=list_id)
        todoitem = Todoitem.objects.get(id=item_id,todo_list=todolist)
        item = Todoitem.objects.filter(id=item_id,todo_list=todolist)
    except Todolist.DoesNotExist:
        raise Http404("this list does not exist")
    except Todoitem.DoesNotExist:
        raise Http404("this item does not exist")
    if request.method == 'GET':
        context = {
        'todolist' : todolist,
        'todoitem' : todoitem
        }
        return render(request, 'todo/updateitem.html',context)
    title1 = request.POST["title"]
    date = request.POST["duedate"]
    if request.POST["status"] == 'on':
        status=True
    else:
        status=False

    item.update(title=title1,checked=status,due_date=date,todo_list=todolist)
    lists = Todolist.objects.all()
    context = {
        'todolists' : lists
    }
    return render(request, 'todo/index.html', context )


def delete_item(request,list_id,item_id):
    try:
        todolist = Todolist.objects.get(id=list_id)
    except Todolist.DoesNotExist:
        raise Http404("this list does not exist")
    try:
        todoitem = Todoitem.objects.get(id=item_id,todo_list=todolist)
        res = Todoitem.objects.filter(id=item_id,todo_list=todolist)
    except Todoitem.DoesNotExist:
        raise Http404("this item does not exist")

    res.delete()
    items_list = Todoitem.objects.filter(todo_list = todolist)
    context = {
        'todolist' : todolist,
        'items_list' : items_list
    }
    return render(request, 'todo/detail.html', context )

def todo_update(request,list_id):
    todolist = Todolist.objects.get(id=list_id)
    data=request.POST
    todoitems = Todoitem.objects.filter(todo_list=todolist)
    todoitems.update(checked=False,todo_list=todolist)
    for item in data:
        try:
            todoitem = Todoitem.objects.get(title=item,todo_list=todolist)
            res = Todoitem.objects.filter(title=item,todo_list=todolist)
            print(res)
            res.update(checked=True,todo_list=todolist)
        except Todoitem.DoesNotExist:
            pass
    lists = Todolist.objects.all()
    context = {
        'todolists' : lists
    }
    return render(request, 'todo/index.html', context )

