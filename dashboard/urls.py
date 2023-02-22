from django.urls import path

from .views import (
    DashboardPostsView, DashboardFollowingTagsView,
    DashboardFollowingUsersView, DashboardFollowersView,
    DashboardReadingListView
)

app_name = "dashboard"

urlpatterns = [
    path('post/', DashboardPostsView.as_view(), name='posts'),
    path('folllowing-tags/', DashboardFollowingTagsView.as_view(), name='following-tags'),
    path('followers/', DashboardFollowersView.as_view(), name='followers'),
    path('following-users/', DashboardFollowingUsersView.as_view(), name='following-users'),
    path('reading-list/', DashboardReadingListView.as_view(), name='reading-list'),
]
