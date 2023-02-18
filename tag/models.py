from django.db import models
from django.urls import reverse_lazy

from users.models import Profile


# Create your models here.


class Tag(models.Model):
    COLORS = [
        ('DF', 'blue'),
        ('DK', 'gray'),
        ('RD', 'red'),
        ('GR', 'green'),
        ('YL', 'yellow'),
        ('ID', 'indigo'),
        ('PP', 'purple'),
        ('PK', 'pink'),
    ]
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256, null=True, blank=True)
    color = models.CharField(max_length=2, choices=COLORS, default='DF')

    def __str__(self):
        return f"# {self.name}"


class FollowingTags(models.Model):
    class Meta:
        default_related_name = 'following_tags'

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.profile} follows {self.tag}'
