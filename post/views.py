from django.shortcuts import render,HttpResponse,get_list_or_404,HttpResponseRedirect,redirect
from .models import post
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import time
def post_index(request):
    posts_list=post.objects.all()
    query=request.GET.get('q')
    if query:
        posts_list=posts_list.filter(Q(baslik__contains=query)|

                                     Q(metin__contains=query)|
                                     Q(user__first_name__contains=query)|
                                     Q(user__last_name__contains=query)
                                     ).distinct()
    # else:
    #     posts_list=posts_list.filter(metin__in=query)
    paginator = Paginator(posts_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request,'post/index.html',{'posts':posts})
def post_detail(request,slug):
    Post =post.objects.get(slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = Post
        comment.save()
        return HttpResponseRedirect(Post.get_absolute_url())
    context={'post':Post,
             'form':form,
             }
    return render(request,'post/detail.html',context)

def post_create(request):
    if not request.user.is_authenticated:
        raise Http404()
    # form=PostForm()
    # if request.method=="POST":
    #    print(request.POST)
    # baslik=request.POST.get("baslik")
    # metin=request.POST.get("metin")
    # post.objects.create(baslik=baslik,metin=metin)
    # if request.method=="POST":#bilgiler ikaydet
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    # else:#formu göst
    #     form = PostForm(re)

    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        Post=form.save(commit=False)
        Post.user=request.user
        Post.save()
        time.sleep(2)
        messages.success(request,'KAYDEDİLDİ')
        return HttpResponseRedirect(Post.get_absolute_url())
    context = {'form': form,
               }
    return render(request,'post/form.html',context)

def post_update(request,slug):
    if not request.user.is_authenticated:
        raise Http404()

    Post = post.objects.get(slug=slug)
    form = PostForm(request.POST or None,request.FILES or None,instance=Post)
    if form.is_valid():
        form.save()
        time.sleep(1)
        messages.success(request, 'GÜNCELLENDİ',extra_tags='mesaj başarılı')
        return HttpResponseRedirect(Post.get_absolute_url())
    context = {'form': form,
               }
    return render(request, 'post/form.html', context)

def post_delete(request,slug):
    Post = post.objects.get(slug=slug)
    Post.delete()
    messages.error(request, 'SİLİNDİ')
    return redirect('post:index')




