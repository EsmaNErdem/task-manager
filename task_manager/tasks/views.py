from django.http import JsonResponse
from .models import Task

def list_tasks(request):
    try:
        # Retrieve all tasks from the database
        tasks = Task.objects.all()

        # Return a JSON response with the formatted data
        return JsonResponse([task.serialize() for task in tasks], safe=False, status=200)
    except Exception as e:
        # Return a custom error response if an exception occurs
        return JsonResponse({'error': str(e)}, status=500)


def task_detail(request, task_id):
    try:
        # retrieve task with given pk
        task = Task.objects.get(pk=task_id)
        
        return JsonResponse(task.serialize(), safe=False, status=200)
    except Task.DoesNotExist:
        # Return a custom error response if the task does not exist
        return JsonResponse({'error': 'Task not found'}, status=404)
    except Exception as e:
        # Return a custom error response for other exceptions
        return JsonResponse({'error': str(e)}, status=500)