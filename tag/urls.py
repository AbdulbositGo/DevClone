from django.urls import path

from .views import Tag


urlpatterns = [
    path('', Tag, name='tags'),
]
