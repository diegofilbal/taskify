from django.contrib import admin
from django.urls import path

from todos.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    MarkAsDoneView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>/", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>/", TodoDeleteView.as_view(), name="todo_delete"),
    path("mark-as-done/<int:pk>/", MarkAsDoneView.as_view(), name="mark_as_done"),
]
