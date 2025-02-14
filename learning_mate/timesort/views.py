from django.shortcuts import render
from .models import Snippet

def snippet_list(request):
    snippets = Snippet.objects.all()  # select_related 제거
    return render(request, 'timesort/snippets_list.html', {'snippets': snippets})

