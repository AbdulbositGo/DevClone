from django.shortcuts import render
from django.views import View

from post.models import Post
from tag.models import FollowingTags


# Create your views here.


class DashboardPostsView(View):
    def get(self, request):
        posts = Post.objects.filter(profile=request.user)
        context = {
            'posts': posts
        }
        return render(request, 'dashboard/posts.html', context)


class DashboardFollowingTagsView(View):
    def get(self, request):
        following_tags = request.user.following_tags.all()
        context = {
            'following_tags': following_tags
        }
        return render(request, 'dashboard/following-tags.html', context)


class DashboardFollowersView(View):
    def get(self, request):
        return render(request, 'dashboard/followers.html')


class DashboardFollowingUsersView(View):
    def get(self, request):
        return render(request, 'dashboard/following-users.html')


class DashboardReadingListView(View):
    def get(self, request):
        return render(request, 'dashboard/reading-list.html')
