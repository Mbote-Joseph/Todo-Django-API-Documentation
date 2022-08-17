from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from todoAPI.models import Todo
from todoAPI.serializers import TodoSerializer

# Create your views here.
class ListTodoAPIView(ListAPIView):
    # Lists all todos from the database
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreateTodoAPIView(CreateAPIView):
    # Creates a new todo in the database
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodoAPIView(UpdateAPIView):
    # Updates a todo in the database
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodoAPIView(DestroyAPIView):
    # Deletes a todo from the database
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer