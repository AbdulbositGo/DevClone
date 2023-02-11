from django.shortcuts import render, redirect
from django.views import View

from tag.models import Tag
from post.models import Post


# Create your views here.


class TagsView(View):
    def get(self, request):
        tag = request.GET.get('tag') if request.GET.get('tag') else ""
        tags = Tag.objects.filter(name__icontains=tag)
        context = {
            'tags': tags,
            'tag': tag
        }
        return render(request, 'tags.html', context)


class TagView(View):
    def get(self, request, pk):
        tag = Tag.objects.filter(pk=pk).first()
        if not tag:
            return redirect('tags')
        related_posts = Post.objects.filter(tags=tag)
        context = {
            'tag': tag,
            'related_posts': related_posts,
        }
        return render(request, 'tag.html', context)
