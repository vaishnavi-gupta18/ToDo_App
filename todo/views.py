from django.http.response import Http404
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.context import Context
from django.views import generic
from .models import Todolist, Todoitem
# Create your views here.
# def index(request):
#     list_todo = Todolist.objects.all()
#     template = loader.get_template('todo/index.html')
#     context = {
#         'todolists' : list_todo,
#     }
#     # output = ', '.join(item.title for item in list_items)
#     return HttpResponse(template.render(context,request))
class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todolists'

    def get_queryset(self):
        return Todolist.objects.all()

# class detail(generic.DetailView):
#     model=Todolist
#     template_name='todo/' 
def detail(request, list_id):
    try:
        todolist = Todolist.objects.get(id=list_id)
    except Todolist.Doesnotexist:
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
    Todolist.objects.create(list_name=name)
    lists = Todolist.objects.all()
    context = {
        'todolists' : lists
    }
    return render(request, 'todo/index.html', context )

def delete(request):
    if request.method == 'GET':
        return render(request, 'todo/deletelist.html')
    
    name = request.POST["name"]
    try:
        todolist = Todolist.objects.get(list_name=name)
    except Todolist.DoesNotExist:
        messages.error(request,'List not present')
        return render(request, 'todo/deletelist.html')
    res = Todolist.objects.filter(list_name=name)
    res.delete()
    lists = Todolist.objects.all()
    context = {
        'todolist' : todolist
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
    Todoitem.objects.create(title=title1,checked=False,due_date=date,todo_list=todolist)
    lists = Todolist.objects.all()
    context = {
        'todolists' : lists
    }
    return render(request, 'todo/index.html', context )