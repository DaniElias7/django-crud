from django.urls import path
from .views import create_task, list_tasks, delete_task

urlpatterns = [
    path('', list_tasks),
    path('new/', create_task, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task')
]