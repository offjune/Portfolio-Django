from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    finished_at = models.DateField(null=True)
    completed = models.BooleanField(default=False)
