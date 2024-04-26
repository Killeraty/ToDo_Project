from django.urls import path

from apps.todo.views import (
    get_all_tasks,
    create_new_task,
    update_task,
    get_task_info_by_id,
    delete_task,
    get_subtasks_info,
    get_subtask_info_by_id,
    update_subtask,
    create_subtask,
    delete_subtask
)

app_name = "tasks"

urlpatterns = [
    path("", get_all_tasks, name='all-tasks'),
    path("subtasks/", get_subtasks_info, name='all-subtasks'),
    path("subtask/<int:subtask_id>/", get_subtask_info_by_id, name='subtask-info'),
    path("subtask/<int:subtask_id>/update/", update_subtask, name='update-subtask'),
    path("subtask/create", create_subtask, name='create-subtask'),
    path("subtask/<int:subtask_id>/delete", delete_subtask, name='delete-subtask'),
    path("create/", create_new_task, name='create-task'),
    path("<int:task_id>/", get_task_info_by_id, name='task-info'),
    path("<int:task_id>/update/", update_task, name='update_task'),
    path("<int:task_id>.delete/", delete_task, name='delete_task'),
]
