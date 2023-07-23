from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, Post, Comment, Like, Notice
from django.contrib.auth.decorators import login_required
from .forms import Userfile
from datetime import datetime
import random
from PIL import Image
import json

thesaurus = []

with open('collection.json', encoding='utf8') as f:
    thesaurus = json.loads(f.read())

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('fan:home')
        else:
            return redirect('fan:login')
    default_avatar = {"img": "default/txdefault.jpg",}
    context = {
        "user": default_avatar,
    }

    return render(request, 'fan/login.html', context)


@login_required(login_url='fan:login')
def home_view(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(owner=user_object)
    notice = Notice.objects.all()
    posts = Post.objects.order_by("-pinned", "-id")
    for i in posts:
        i.likes = Like.objects.filter(post=i).count()
    context = {
        "user": user_profile,
        "posts": posts,
        "thesaurus": random.choice(thesaurus),
        "notice": notice,
    }
    return render(request, 'fan/home.html', context)


def register_view(request):
    default_avatar = {"img": "default/txdefault.jpg",}
    context = {
        "user": default_avatar,
    }
    if request.method == 'POST':
        username = request.POST['username']
        nike_name = request.POST['nike_name']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        user_model = User.objects.get(username=username)
        new_userprofile = UserProfile.objects.create(owner=user_model, nike_name=nike_name)
        new_userprofile.save()
        return redirect('fan:login')
    else:
        return render(request, 'fan/register.html', context)


@login_required(login_url='fan:login')
def editarticle_view(request):
    if request.method == 'POST':
        content = request.POST['content']
        show_view = request.POST.get('show_view', False)
        if show_view == 'true':
            show_view = True
        user_object = User.objects.get(username=request.user.username)
        user_profile = UserProfile.objects.get(owner=user_object)
        new_post = Post.objects.create(post_owner=user_object, post_content=content, owner_profile=user_profile, show_view=show_view)
        new_post.post_img1 = request.FILES.get('post_img')
        new_post.save()
        path = './media/' + str(new_post.post_img1)
        im = Image.open(path)
        (x, y) = im.size
        x1 = 512
        y1 = int(y * x1 / x)
        path1 = './thumbnail/' + str(new_post.post_img1)
        out = im.resize((x1, y1), Image.ANTIALIAS)
        out.save(path1)
        return redirect('fan:home')

@login_required(login_url='fan:login')
def post_detail_view(request, post_id):
    user_object = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(owner=user_object)
    post = Post.objects.get(id=post_id)
    comment_list = Comment.objects.filter(post=post)
    like_list = Like.objects.filter(post=post)
    liked = 0
    for i in like_list:
        if i.user == user_object:
            liked = 1
    context = {
        "user": user_profile,
        "liked": liked,
        "post": post,
        "owner": post.post_owner,
        "owner_profile": post.owner_profile,
        "comment_list": comment_list,
        "content": post.post_content,
    }
    if request.method == 'POST':
        text = request.POST['comment_text']
        if text:
            new_comment = Comment.objects.create(user=user_profile, post=post, text=text)
            new_comment.save()

        return redirect('fan:post_detail', post_id=post_id)
    else:
        return render(request, 'fan/article_detail.html', context)


@login_required(login_url='fan:login')
def user_page_view(request):
    user = User.objects.get(username=request.user.username)
    profile = UserProfile.objects.get(owner=user)
    context = {
        "user": profile
    }
    return render(request, 'fan/user_page.html', context)

@login_required(login_url='fan:login')
def logout_view(request):
    logout(request)
    return redirect('fan:login')

@login_required(login_url='users:login')
def edit_profile_view(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(owner=user_object)
    context = {
        "user": user_profile
    }
    if request.method == 'POST':
        if request.POST['nike_name']:
            user_profile.nike_name = request.POST['nike_name']
        if request.POST['desc']:
            user_profile.desc = request.POST['desc']
        if request.POST['sign']:
            user_profile.sign = request.POST['sign']
        if request.POST['address']:
            user_profile.address = request.POST['address']
        if request.FILES.get('img'):
            user_profile.img = request.FILES.get('img')
        if request.FILES.get('backimg'):
            user_profile.back_img = request.FILES.get('backimg')
        if request.POST['birthday']:
            user_profile.birthday = datetime.strptime(request.POST['birthday'], "%Y-%m-%d")
        user_profile.save()
        return redirect('fan:user_page')
    else:
        return render(request, 'fan/edit_user.html', context)

@login_required(login_url='users:login')
def others_page_view(request, user_id):
    user = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(owner=user)
    target = User.objects.get(id=user_id)
    target_profile = UserProfile.objects.get(owner=target)
    context = {
        "target": target,
        "target_profile": target_profile,
        "user": user_profile,
    }
    # redirect('fan:others_page', user_id=user_id)
    return render(request, 'fan/others_page.html', context)

@login_required(login_url='fan:login')
def post_like(request, post_id):
    user = User.objects.get(username=request.user.username)
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        if Like.objects.filter(post=post, user=user).count() == 0:
            Like.objects.create(user=user, post=post)
            return HttpResponse("点赞成功")
        else:
            Like.objects.filter(user=user, post=post).delete()
            return HttpResponse("取消点赞")