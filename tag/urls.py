from django.urls import path

from .views import TagsView


urlpatterns = [
    path('', TagsView.as_view(), name='tags'),
]
