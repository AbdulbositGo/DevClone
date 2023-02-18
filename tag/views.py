from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse, render, redirect
from django.views import View

from tag.models import Tag, FollowingTags
from post.models import Post


# Create your views here.


class TagsView(View):
    def get(self, request):
        tag = request.GET.get('tag') if request.GET.get('tag') else ""
        tags = Tag.objects.filter(name__icontains=tag)
        following_tags = request.user.following_tags.all()
        following_tags_ids = [tag.tag.id for tag in following_tags]
        context = {
            'tags': tags,
            'tag': tag,
            'following_tags_ids': following_tags_ids
        }
        return render(request, 'tags.html', context)


class TagView(View):
    def get(self, request, pk):
        tag = Tag.objects.filter(pk=pk).first()
        if not tag:
            return redirect('tags')

        related_posts = Post.objects.filter(tags=tag)
        following_tags = request.user.following_tags.all()
        following_tags_ids = [tag.tag.id for tag in following_tags]
        context = {
            'tag': tag,
            'related_posts': related_posts,
            'following_tags_ids': following_tags_ids,
        }
        return render(request, 'tag.html', context)


class FollowingTagView(View, LoginRequiredMixin):
    def get(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        if not tag:
            return redirect(reverse("tags"))
        if request.user.following_tags.filter(profile=request.user, tag=tag).exists():
            follow_obj = FollowingTags.objects.get(profile=request.user, tag=tag)
            follow_obj.delete()
        else:
            FollowingTags.objects.create(profile=request.user, tag=tag)
        return redirect(reverse('tag', kwargs={'pk': tag.id}))
