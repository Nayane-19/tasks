from django.urls import path

from . import views

urlpatterns = [
    path('helloworld', views.helloWorld),
    path('', views.todoList, name='todo-list')
]
