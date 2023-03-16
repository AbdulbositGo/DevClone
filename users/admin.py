from django.contrib import admin

from .forms import ProfileModelForm
from .models import Profile, Follow, Basic, Work, Coding


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileModelForm


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follow)
admin.site.register(Basic)
admin.site.register(Coding)
admin.site.register(Work)
