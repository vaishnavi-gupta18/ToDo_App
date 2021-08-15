from django.urls import path
from todo.views import IndexView, detail,create,delete,create_item, todo_update,update,update_item,delete_item,todo_update
app_name='todo'
urlpatterns = [
    # path('', index, name='index'),
    path('',IndexView.as_view(), name='index'),
    path('<int:list_id>/', detail, name='list_detail'),
    path('create/',create,name='list_create'),
    path('<int:list_id>/delete',delete,name='list_delete'),
    path('<int:list_id>/updatelist',update,name='list_update'),
    path('<int:list_id>/createitem/',create_item,name='item_create'),
    path('<int:list_id>/<int:item_id>/',update_item,name='item_update'),
    path('<int:list_id>/<int:item_id>/delete',delete_item,name='item_delete'),
    path('<int:list_id>/update',todo_update,name='update')

]
