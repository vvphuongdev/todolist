from django.db import models
from django.utils import timezone
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title