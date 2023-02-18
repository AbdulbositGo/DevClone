from django.urls import path

from .views import TagsView, TagView, FollowingTagView


urlpatterns = [
    path('tags/', TagsView.as_view(), name='tags'),
    path('tag/<int:pk>', TagView.as_view(), name='tag'),
    path('tag/<int:pk>/following', FollowingTagView.as_view(), name='following-tag'),
]
