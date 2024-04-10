from django.urls import path
from . import views

urlpatterns = [
    # /tasks
    path('', views.list_tasks, name='list_tasks'),
    # /tasks/id
    path('<int:task_id>/', views.task_detail, name='task_detail'),
]
