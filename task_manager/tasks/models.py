from django.db import models

PRIORITY_CHOICES = [
    (1, 'Can wait'),
    (2, 'Important'),
    (3, 'Get to work'),
]

class Task(models.Model):
    # taskOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    taskName = models.CharField(max_length=100, default='task')
    dueDate = models.DateField()
    priority = models.CharField(choices=PRIORITY_CHOICES, default=1)

    def __str__(self):
        """String representation of table column"""

        return f"{self.taskName}, due by {self.dueDate} with {self.priority} priority"