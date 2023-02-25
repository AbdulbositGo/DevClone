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
        followers = request.user.followers.all()
        context = {
            'followers': followers
        }
        return render(request, 'dashboard/followers.html', context)


class DashboardFollowingUsersView(View):
    def get(self, request):
        following = request.user.following.all()
        context = {
           'following': following
        }
        return render(request, 'dashboard/following-users.html', context)


class DashboardReadingListView(View):
    def get(self, request):
        reading_list = request.user.readinglist_set.all()
        context = {
            'reading_list': reading_list
        }
        return render(request, 'dashboard/reading-list.html', context)
