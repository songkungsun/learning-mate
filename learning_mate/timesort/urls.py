from django.urls import path
from .views import snippet_list

app_name = 'timesort'

urlpatterns = [
    path('snippets/', snippet_list, name='snippet_list'),
]

