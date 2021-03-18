from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import ToDoList
from .serializers import ToDoListSerializer


class ToDoListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todolist = ToDoList.objects.filter(user=request.user)
        serializer = ToDoListSerializer(todolist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToDoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoListDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, request, pk):
        try:
            return ToDoList.objects.filter(user=request.user).get(pk=pk)
        except ToDoList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        todo = self.get_object(request, pk)
        serializer = ToDoListSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(request, pk)
        serializer = ToDoListSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(request, pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
