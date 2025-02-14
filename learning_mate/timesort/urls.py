from django.urls import path
from .views import sorted_snippets

urlpatterns = [
    path('', sorted_snippets, name='sorted_snippets'),
]
