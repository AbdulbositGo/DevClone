from post.models import Post
from tag.models import FollowingTags
from users.models import Follow


def dashboard_count_info(request):
    if request.user.is_authenticated:
        following = request.user.following.all()
        following_username = [user.following.username for user in following]
        context = {
            'post_count': Post.objects.filter(profile=request.user).count(),
            'following_tag_count': FollowingTags.objects.filter(profile=request.user).count(),
            'following_count': Follow.objects.filter(follower=request.user).count(),
            'follower_count': Follow.objects.filter(following=request.user).count(),
            'following_username': following_username
        }
        return context
    return {}
