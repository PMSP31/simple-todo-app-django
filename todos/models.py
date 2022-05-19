from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Todo(models.Model):
    LIST_STATUS = (
        ('VI', 'Very Important'),
        ('I', 'Important'),
        ('N', 'Normal')
    )

    task = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=50,
        default='very_important',
        choices = LIST_STATUS
        )
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse_lazy('index')

    def save(self) :
        super().save()

    def __str__(self):
        return f"{self.id}. {self.task} | {self.status}"