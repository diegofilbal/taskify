from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]
