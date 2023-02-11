from django.urls import path

from .views import HomeView, CreatePostView, PostView, postUpdate


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<str:username>/<int:pk>/', PostView.as_view(), name='post'),
    path('<str:username>/<int:pk>/updat/', postUpdate, name='post-update'),
    path('new-post', CreatePostView.as_view(), name='new-post'),
]
