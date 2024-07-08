from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from post.forms import PostForm
from post.models import Post


class PostListView(View):
    def get(self, request):
        posts = Post.objects.select_related('creator').all()
        return render(request, template_name='post/post_list.html', context={'posts': posts})


class PostView(View):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            return render(request, 'post/post.html', context={'post': post})
        except Post.DoesNotExist:
            raise Http404


class UserPostView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = PostForm()
        posts = Post.objects.filter(creator=request.user)
        return render(request, 'post/user_post_list.html', context={'form': form, 'posts': posts})

    @method_decorator(login_required)
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.save()
            return redirect('create_post')
        posts = Post.objects.filter(creator=request.user)
        return render(request, 'post/user_post_list.html', context={'form': form, 'posts': posts})
