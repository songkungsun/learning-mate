from django.db import models

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    username_normalized = models.CharField(max_length=255, blank=True, null=True)
    password_hash = models.CharField(max_length=255)
    oidc_id = models.CharField(max_length=255, blank=True, null=True)
    oidc_provider = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Snippet(models.Model):
    title = models.TextField()
    description = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)  # 시간순 정렬을 위해
    user = models.ForeignKey(User, related_name="snippets", on_delete=models.CASCADE)  # user와 관계 설정
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Category(models.Model):
    snippet = models.ForeignKey(Snippet, related_name="categories", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Fragment(models.Model):
    snippet = models.ForeignKey(Snippet, related_name="fragments", on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    code = models.TextField()
    language = models.CharField(max_length=50)
    position = models.IntegerField()

    def __str__(self):
        return self.file_name

class SharedSnippet(models.Model):
    snippet = models.ForeignKey(Snippet, related_name="shared_snippets", on_delete=models.CASCADE)
    requires_auth = models.BooleanField(default=False)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shared Snippet {self.snippet.title}"

