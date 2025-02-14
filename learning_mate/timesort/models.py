from django.db import models

class Snippet(models.Model):
    title = models.TextField()
    description = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)  # 시간순 정렬을 위해
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title
