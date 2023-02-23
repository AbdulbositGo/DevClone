from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from django.views import View

from post.models import Post
from .forms import (
    ProfileModelForm, WorkModelForm, CodingModelForm,
    BasicModelForm, RegistrationForm, LoginForm
)
from .models import Profile, Follow


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {
            'form': form
        }
        return render(request, 'registration.html', context)

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {
                'form': form
            }
            return render(request, 'registration.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next = request.GET.get('next') if request.GET.get('next') else ''
            return redirect('home' + next)
        else:
            context = {
                'form': form
            }
            return render(request, 'login.html', context)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'logout.html')

    def post(self, request):
        logout(request)
        return redirect(reverse('home'))


class ProfileView(View):
    def get(self, request, username):
        profile = get_object_or_404(Profile, username=username)
        posts = profile.post_set.all()
        comments = profile.comment_set.all()
        if request.user.is_authenticated:
            following = request.user.following.all()
            following_username = [user.following.username for user in following]
        else:
            following_username = []
        if profile:
            context = {
                'profile': profile,
                'posts': posts,
                'comments': comments,
                'following_username': following_username
            }
            return render(request, 'profile.html', context)
        return redirect(reverse('home'))


class FollowToggle(LoginRequiredMixin, View):
    def post(self, request, username, *args, **kwargs):
        following_user = get_object_or_404(Profile, username=username)
        if request.user.following.filter(following=following_user).exists():
            follow_obj = Follow.objects.get(follower=request.user, following=following_user)
            follow_obj.delete()
        else:
            follow_obj = Follow(follower=request.user, following=following_user)
            follow_obj.save()

        return redirect('profile', username=following_user.username)


class SettingsView(LoginRequiredMixin, View):
    def get(self, request):
        profile = Profile.objects.get(username=request.user.username)

        profile_form = ProfileModelForm(instance=profile)
        basic_form = BasicModelForm(instance=profile.basic)
        coding_form = CodingModelForm(instance=profile.coding)
        work_form = WorkModelForm(instance=profile.work)
        context = {
            'profile': profile,
            'profile_form': profile_form,
            'basic_form': basic_form,
            'coding_form': coding_form,
            'work_form': work_form,
        }
        return render(request, "settings.html", context)

    def post(self, request):
        profile = Profile.objects.get(username=request.user.username)
        profile_form = ProfileModelForm(data=request.POST, files=request.FILES, instance=profile)
        basic_form = BasicModelForm(data=request.POST or None, instance=profile.basic)
        coding_form = CodingModelForm(data=request.POST or None, instance=profile.coding)
        work_form = WorkModelForm(data=request.POST or None, instance=profile.work)

        if profile_form.is_valid() and basic_form.is_valid() and coding_form.is_valid() and work_form.is_valid():

            for form in [profile_form, basic_form, coding_form, work_form]:
                form.save()

        return redirect('settings')


