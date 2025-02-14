from django.shortcuts import render
from .models import Snippet

def sorted_snippets(request):
    # 바이트스태쉬 DB에서 데이터를 시간순으로 정렬하여 가져오기
    snippets = Snippet.objects.using('bytestash').order_by('-updated_at')
    return render(request, 'timesort/sorted_list.html', {'snippets': snippets})
