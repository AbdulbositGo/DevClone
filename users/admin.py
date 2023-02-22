from django.contrib import admin

from .models import Profile, Follow, Basic, Work, Coding
# Register your models here.


admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Basic)
admin.site.register(Coding)
admin.site.register(Work)
