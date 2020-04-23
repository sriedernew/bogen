from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import PostForm
from .models import Post
from .models import Category

# Create your views here.
def post_list(request):
    viewname = 'blog'
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts,'viewname':viewname})

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

def forbidden(request):
    return redirect('post_list')

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def get404(request):
    return render(request, '404.html')
