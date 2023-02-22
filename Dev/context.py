from post.models import Post
from tag.models import Tag, FollowingTags


def dashboard_count_info(request):
    context = {
        'post_count': Post.objects.filter(profile=request.user).count(),
        'following_tag_count': FollowingTags.objects.filter(profile=request.user).count(),
    }
    return context
