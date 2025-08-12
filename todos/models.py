from datetime import datetime
from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    deadline = models.DateField(verbose_name="Prazo", null=False, blank=False)
    finished_at = models.DateField(verbose_name="Concluído em", null=True, blank=True)

class Meta:
    ordering = ["deadline"]

    def mark_as_completed(self):
        self.finished_at = datetime.now()
        self.save()