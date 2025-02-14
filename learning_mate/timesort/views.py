from django.shortcuts import render
from .models import ByteStashSnippet

def sorted_snippets(request):
    snippets = ByteStashSnippet.objects.using('bytestash').order_by('-updated_at')
    return render(request, 'timesort/sorted_list.html', {'snippets': snippets})
