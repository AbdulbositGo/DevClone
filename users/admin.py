from django.contrib import admin

from .forms import ProfileModelForm
from .models import Profile, Follow, Basic, Work, Coding


admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Basic)
admin.site.register(Coding)
admin.site.register(Work)
