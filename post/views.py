from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from post.forms import PostModelForm, CommentModelForm
from post.models import Post
from users.models import Profile


# Create your views here.

class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()

        context = {
            'posts': posts
        }
        return render(request, 'home.html', context)


class PostView(View):
    def get(self, request, pk, username):
        post_obj = Post.objects.get(pk=pk)
        if post_obj is None:
            return redirect('/')
        form = CommentModelForm()
        context = {
            'post': post_obj,
            'form': form
        }
        return render(request, 'post.html', context)

    def post(self, request, pk):
        if request.user.is_authunticated:
            form = CommentModelForm(data=request.POST or None)
            post_obj = Post.objects.get(pk=pk)
            profile = Profile.objects.get(username=request.user.username)

            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = post_obj
                new_comment.profile = profile
                form.save()
                return redirect('post', post_obj.profile.username, post_obj.pk)
        else:
            return redirect('login')

class CreatePostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request, 'post-create.html', context)

    def post(self, request):
        form = PostModelForm(data=request.POST or None, files=request.FILES)
        profile = Profile.objects.get(username=request.user.username)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.profile = profile
            new_post.save()
            form.save_m2m()
            return redirect('post', new_post.profile.username, new_post.pk)


def postUpdate(request, pk, username):
    obj = Post.objects.filter(pk=pk).first()
    if not obj:
        return redirect('home')
    form = PostModelForm(data=request.POST or None, files=request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('post')

    else:
        form = PostModelForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'post-update.html', context)
