from post.models import Post
from tag.models import Tag, FollowingTags
from users.models import Follow


def dashboard_count_info(request):
    if request.user.is_authenticated:
        context = {
            'post_count': Post.objects.filter(profile=request.user).count(),
            'following_tag_count': FollowingTags.objects.filter(profile=request.user).count(),
            'following_count': Follow.objects.filter(follower=request.user).count(),
            'follower_count': Follow.objects.filter(following=request.user).count(),
        }
        return context
    return {}