from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default="")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
