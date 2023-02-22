from django.shortcuts import render
from django.views import View


# Create your views here.


class DashboardPostsView(View):
    def get(self, request):
        return render(request, 'dashboard/posts.html')


class DashboardFollowingTagsView(View):
    def get(self, request):
        return render(request, 'dashboard/following-tags.html')


class DashboardFollowersView(View):
    def get(self, request):
        return render(request, 'dashboard/followers.html')


class DashboardFollowingUsersView(View):
    def get(self, request):
        return render(request, 'dashboard/following-users.html')


class DashboardReadingListView(View):
    def get(self, request):
        return render(request, 'dashboard/reading-list.html')
