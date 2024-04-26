from django.urls import path, include

from apps.todo.views import Home_page

app_name = 'router'

urlpatterns = [
    path("user/", include('apps.user.urls')),
    path("", Home_page, name='home'),
    path("tasks/", include('apps.todo.urls')),
    path("api/", include('apps.api.urls')),
]


