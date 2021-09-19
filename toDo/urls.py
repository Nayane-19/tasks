from django.urls import path

from . import views

urlpatterns = [
    path('helloworld', views.helloWorld),
    path('', views.todoList, name='todo-list'),
    path('toDo/<int:id>', views.todoView, name='todo-view'),
    path('newtask/', views.newTask, name='new-task'),
    path('edit/<int:id>', views.editTask, name='edit-task'),
    path('delete/<int:id>', views.deleteTask, name='delete-task'),
]
