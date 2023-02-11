from django.shortcuts import render
from django.views import View

from tag.models import Tag


# Create your views here.


class TagsView(View):
    def get(self, request):
        tags = Tag.objects.all()
        context = {
            'tags': tags
        }
        return render(request, 'tags.html', context)
