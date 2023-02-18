from django.contrib import admin

from tag.models import Tag, FollowingTags

# Register your models here.

admin.site.register(Tag)
admin.site.register(FollowingTags)
