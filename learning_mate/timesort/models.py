from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    username_normalized = models.CharField(max_length=255, null=True, blank=True)
    password_hash = models.CharField(max_length=255)
    oidc_id = models.CharField(max_length=255, null=True, blank=True)
    oidc_provider = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'snippets'

    def __str__(self):
        return self.title

class Category(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Fragment(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    code = models.TextField()
    language = models.CharField(max_length=50)
    position = models.IntegerField()

    def __str__(self):
        return f'{self.file_name} - {self.language}'

class SharedSnippet(models.Model):
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    requires_auth = models.BooleanField(default=False)
    expires_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shared: {self.snippet.title}"

