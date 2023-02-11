from django.urls import path

from .views import TagsView, TagView


urlpatterns = [
    path('tags/', TagsView.as_view(), name='tags'),
    path('tag/<int:pk>', TagView.as_view(), name='tag'),
]
