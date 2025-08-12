from django.contrib import admin
from django.urls import path, include

from todos.views import TodoCreateView, TodoListView, TodoUpdateView, TodoDeleteView, TodoCompletedView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("completed/<int:pk>", TodoCompletedView.as_view(), name="todo_completed")
]