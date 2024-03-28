from django.http import JsonResponse

def list_tasks(request):
    data = {
        'task1': 'value1'
    }
    # Return a JSON response with a custom status code
    return JsonResponse(data, status=200)
