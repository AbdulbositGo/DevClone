from django.contrib import admin

from .models import Profile, Basic, Work, Coding
# Register your models here.


admin.site.register(Profile)
admin.site.register(Basic)
admin.site.register(Coding)
admin.site.register(Work)