from django.http import JsonResponse
from .models import Task

def list_tasks(request):
    # Retrieve all tasks from the database
    tasks = Task.objects.all()

    # Return a JSON response with the formatted data
    return JsonResponse([task.serialize() for task in tasks], status=200)


def task_detail(request, task_id):
    # retrieve task with given pk
    task = Task.objects.get(pk=task_id)
    
    return JsonResponse(task.serialize(), status=200)