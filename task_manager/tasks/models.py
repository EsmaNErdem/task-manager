from django.db import models

PRIORITY_CHOICES = [
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High'),
]

class Task(models.Model):
    # taskOwner = models.ForeignKey(User, on_delete=models.CASCADE)    taskName = models.CharField(max_length=100)
    dueDate = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)

