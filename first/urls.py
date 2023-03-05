from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import NameList

urlpatterns = [
    path('name/', NameList.as_view())
]
