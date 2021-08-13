from django.db import models

# Create your models here.

class Todolist(models.Model):
    list_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.list_name}"


class Todoitem(models.Model):
    title = models.CharField(max_length=100)
    checked = models.BooleanField(default=False)
    due_date = models.DateTimeField(null = True)

    todo_list = models.ForeignKey(to=Todolist, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.todo_list.list_name}: {self.title}"