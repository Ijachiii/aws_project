from django.db import models

# Create your models here.
class Process(models.Model):
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    status = models.CharField(default="queued")
    result = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.created_at}"