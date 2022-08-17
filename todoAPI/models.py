from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=200)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title