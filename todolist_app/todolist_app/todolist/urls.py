from django.urls import path
from . import views


urlpatterns = [
    path('todolist/', views.ToDoListAPIView.as_view(), name='todolist'),
    path('todolist/<int:pk>/', views.ToDoListDetailAPIView.as_view(), name='todo')
]