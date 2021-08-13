from django.contrib import admin
from .models import Todoitem, Todolist
# Register your models here.
admin.site.register(Todoitem)
admin.site.register(Todolist)
