from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add_task/', add_task, name='add_task'),
    path('mark_as_done/<int:task_id>/', mark_as_done, name='mark_as_done'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('pending_tasks/<int:task_id>/', pending_tasks, name='pending_tasks'),


]
