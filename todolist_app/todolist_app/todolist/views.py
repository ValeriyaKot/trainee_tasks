from .models import ToDoList
from .serializers import ToDoListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from account.permissions import IsOwner


class ToDoListListCreateView(ListCreateAPIView):
    serializer_class = ToDoListSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def get_queryset(self):
        user = self.request.user
        return ToDoList.objects.filter(user=user)


class ToDoListDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoListSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    queryset = ToDoList.objects.all()
