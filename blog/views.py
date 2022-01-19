from blog.forms import FeedbackForm, PostForm
from .models import Post
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def BlogDetails(request, slug):
    post = Post.objects.get(slug=slug)
    if post.status == 1 or post.author == request.user:
        return render(request, 'post_detail.html', {'post': post, 'form': FeedbackForm()})
    else:
        messages.error(request, 'You are not authorized to view this post')
        return redirect('/articles')

def BlogHome(request):
    posts = Post.objects.filter(status=1) .order_by('-created_date')
    return render(request, 'home.html',{'posts': posts})

@login_required
def CreateBlog(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/articles/')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

@login_required
def BlogUpdate(request, slug):
    post = Post.objects.get(slug=slug)
    if post.author == request.user:
        if request.method == 'POST':    
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect(request.GET.get('next', '/'))
        else:
            form = PostForm(instance=post)
    
        return render(request, 'post_create.html', {'form': form})
    else:
        messages.error(request, 'You are not authorized to edit this post')
        return redirect('/articles')
@login_required
def BlogDelete(request, slug):
    post = Post.objects.get(slug=slug)
    if(post.author == request.user):
        post.delete()
        return redirect('/articles/')
    else:
        messages.error(request, 'You are not authorized to delete this post')
        return redirect('/articles')

@login_required
def GetAllBlogByUser(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_date')
    return render(request, 'home.html', {'posts': posts})

def FeedBackCreate(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_create.html', {'form': form})

def error_404(request, exception):
    return redirect('/articles')

def error_500(request):
    return (redirect('/articles'))