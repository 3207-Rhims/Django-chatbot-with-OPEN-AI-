from django.urls import re_path
from .views import fbbotView

urlpatterns = [
    re_path(r'^0a5479d09ed6f3a78608538ff4787192d7da1012983edeca5/$', fbbotView.as_view(), name='fbbotView')
]
