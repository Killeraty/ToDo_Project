from django.contrib import admin

from apps.todo.models import (
    Task,
    SubTask,
    Status,
    Category
)


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'creator', 'created_at')
    list_filter = ('category', 'status', 'creator', 'created_at')
    search_fields = ('title',)


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'creator', 'created_at')
    list_filter = ('category', 'status', 'creator', 'created_at')
    search_fields = ('title',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)