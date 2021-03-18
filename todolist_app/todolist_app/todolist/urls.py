from django.urls import path
from . import views


urlpatterns = [
    path('todolist/', views.ToDoListListCreateView.as_view(), name='todolist'),
    path('todolist/<int:pk>/', views.ToDoListDetailView.as_view(), name='todo')
]