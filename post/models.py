from django.contrib.auth.models import User
from django.db import models

from users.models import Profile
from tag.models import Tag


# Create your models here.


class Post(models.Model):
    class Meta:
        ordering = ['-created', 'updated']

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post_images", null=True, blank=True)
    title = models.CharField(max_length=150)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        ordering = ['-created']

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
