from django.urls import path
from .views import (
    Home,
    TagsView,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    TagsCreate,
    TagsUpdate,
    TagsDelete,
    toggle_done,
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("tags/", TagsView.as_view(), name="tags_list"),
    path("/create/", TaskCreate.as_view(), name="task_create"),
    path("task/<int:pk>/update/", TaskUpdate.as_view(), name="update_task"),
    path("task/<int:pk>/delete/", TaskDelete.as_view(), name="delete_task"),
    path("tags/create/", TagsCreate.as_view(), name="tag_create"),
    path("tags/<int:pk>/update/", TagsUpdate.as_view(), name="update_tag"),
    path("tags/<int:pk>/delete/", TagsDelete.as_view(), name="delete_tag"),
    path("task/<int:pk>/toggle_done/", toggle_done, name="toggle_done"),
]

app_name = "to_do"
