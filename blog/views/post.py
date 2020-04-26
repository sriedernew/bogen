from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from ..forms import PostForm
from ..models import Post
from ..models import Category

# Create your views here.
def post_list(request):
    viewname = 'blog'
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    entrys = posts.filter(tag__contains = 'Spikzettel')
    return render(request, 'blog/post_list.html', {'posts': posts,'viewname':viewname,'entrys':entrys,'box_title':'Python-Spikzettel'})

def home_list(request):
    viewname = 'home'
    posts = Post.objects.filter(category__name='Home').filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/home_list.html', {'posts': posts,'viewname':viewname})

def post_detail(request, pk):
    codes = False
    post = get_object_or_404(Post, pk=pk)
    if ("code:" in post.text):
        codes = post.text.split("--")
    return render(request, 'blog/post_detail.html', {'post': post, 'codes': codes})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def kontakt(request):
    viewname = 'kontakt'
    post = get_object_or_404(Post, tag__contains = 'Kontakt')
    return render(request, 'blog/post_detail.html', {'post': post,'viewname':viewname})

