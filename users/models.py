from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(AbstractUser):
    display_email = models.BooleanField(default=False)
    image = models.ImageField(default="default_user_image.webp", upload_to='user_images')

    def __str__(self):
        return self.username


class Basic(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    site = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile}'s basic"


class Coding(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    current = models.CharField(max_length=200, null=True, blank=True)
    skills = models.CharField(max_length=200, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile}'s coding"


class Work(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    work = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile}'s work"


@receiver(post_save, sender=Profile)
def create_user_profile_basic(sender, instance, created, *args, **kwargs):
    if created:
        profile_basic_data = [Basic, Coding, Work]
        for basic in profile_basic_data:
            new_basic = basic.objects.create(
                profile=instance
            )
            new_basic.save()
