from django.contrib import admin
from .models import Tag, Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("content",
                    "created_at",
                    "deadline",
                    "is_done", )
    search_fields = ("content", )
    list_filter = ("is_done", "tags", )


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Task, TaskAdmin)
admin.site.register(Tag, TagAdmin)
