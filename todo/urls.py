from django.urls import path
from todo.views import IndexView, detail,create,delete,create_item
app_name='todo'
urlpatterns = [
    # path('', index, name='index'),
    path('',IndexView.as_view(), name='index'),
    path('<int:list_id>/', detail, name='list_detail'),
    path('create/',create,name='list_create'),
    path('delete/',delete,name='list_delete'),
    path('<int:list_id>/createitem/',create_item,name='item_create')
]
