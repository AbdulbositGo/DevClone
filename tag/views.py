from django.shortcuts import render
from django.views import View

from tag.models import Tag


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
