from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post,Category,Tag
import markdown
# Create your views here.

# def index(request):
# 	content = {
# 		'title':'我的博客首页',
# 		'welcome':'欢迎访问我的博客首页'

# 	}
# 	return render(request, 'blog/index.html', context = content)


def index(request):
	post_list = Post.objects.all().order_by('-created_time')
	return render(request, 'blog/index.html', context = {'post_list':post_list})

def detail(request, pk):
	post = get_object_or_404(Post, pk = pk)
	post.body = markdown.markdown(post.body, extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

	return render(request, 'blog/detail.html', context = {'post':post})



def archive(request, year, month):
	post_list = Post.objects.filter(created_time__year=year, created_time__month=month).order_by('-created_time')
	return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
	cate = get_object_or_404(Category, pk = pk)
	post_list = Post.objects.filter(category = cate).order_by('-created_time')
	return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, pk):
	t = get_object_or_404(Tag, pk = pk)
	post_list = Post.objects.filter(tags = t).order_by('-created_time')
	return render(request, 'blog/index.html', context = {'post_list':post_list})



















