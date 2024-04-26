from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Task(models.Model):
    title = models.CharField(
        max_length=75,
        unique=True)
    description = models.TextField(max_length=1500)
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET(1)
    )
    date_started = models.DateField(
        help_text="Начало задачи!"
    )
    deadline = models.DateField(
        help_text="Закрытие задачи!"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.title[:7]}..."

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class SubTask(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=1500)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='subtask'
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET(1)
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    date_started = models.DateField()
    deadline = models.DateField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title[:7]}..."

    class Meta:
        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'
