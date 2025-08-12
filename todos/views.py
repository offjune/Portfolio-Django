from datetime import datetime
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy


from .models import Todo


class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline", "finished_at"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return redirect(reverse_lazy('todo_list'))

class TodoCompletedView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_as_completed()
        return redirect(reverse_lazy('todo_list'))
