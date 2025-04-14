from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Tag, Task


# Create your views here.
# def home(request: HttpRequest) -> HttpResponse:
#     description = Task.objects.filter()
class Home(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "to_do/task_list.html"

    def get_queryset(self):
        return Task.objects.all().order_by('is_done', '-created_at')


class TagsView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "to_do/tags_list.html"


class TagsCreate(generic.CreateView):
    model = Tag
    fields = "__all__"
    context_object_name = "tag_create"
    template_name = "to_do/tag_create.html"
    success_url = reverse_lazy("to_do:tags_list")


class TagsUpdate(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "to_do/tag_update.html"
    success_url = reverse_lazy("to_do:tags_list")


class TagsDelete(generic.DeleteView):
    model = Tag
    template_name = "to_do/tag_confirm_delete.html"
    success_url = reverse_lazy("to_do:home")


class TaskCreate(generic.CreateView):
    model = Task
    fields = "__all__"
    context_object_name = "task_create"
    template_name = "to_do/task_create.html"
    success_url = reverse_lazy("to_do:home")


class TaskUpdate(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "to_do/task_update.html"
    success_url = reverse_lazy("to_do:home")

class TaskDelete(generic.DeleteView):
    model = Task
    template_name = "to_do/task_confirm_delete.html"
    success_url = reverse_lazy("to_do:home")


def toggle_done(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.is_done = not task.is_done
        task.save()
    return redirect(request.META.get('HTTP_REFERER', 'task_list'))
