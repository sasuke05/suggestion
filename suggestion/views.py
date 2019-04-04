from django.shortcuts import render,redirect
from .forms import PostForm, PostReply
from .models import Post,Reply
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts= Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'suggestion/post_list.html', {'posts': posts})

def post_open(request, pk):
    post= Post.objects.get(pk=pk)
    form=PostForm()
    return render(request, 'suggestion/post_open.html', {'post': post, 'form': form })

def post_new(request):
    
    if request.method=="POST":
        form= PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('post_open', pk=post.pk)
    else:
        form= PostForm()
    return render(request, 'suggestion/post_new.html', {'form':form})

def post_comment(request, pk):
    post= Post.objects.get(pk=pk)
    if request.method=="POST":
        f=PostReply(request.POST)
        if f.is_valid():
            comment=f.save(commit=False)
            comment.created_date=timezone.now()
            comment.postno=post
            comment.save()
            return redirect('post_open', pk=post.pk)
    else:
        f= PostReply()
    return render(request, 'suggestion/post_comment.html', {'post': post, 'f':f })
    