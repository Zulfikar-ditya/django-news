from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from .models import Blog, Category


def index(request):
    getData = Blog.objects.filter(status=True).order_by('date_add')
    paginator = Paginator(getData, 20)
    pageNum = request.GET.get('page')
    data_result = paginator.get_page(pageNum)
    return render(request, 'home/index.html', {
        'data': data_result,
    })


def post_detail(request, id):
    try:
        getPost = Blog.objects.get(pk=id, status=True)
    except:
        return redirect('home:404')
    getPostCategory = getPost.categorie
    related_post = Blog.objects.filter(categorie=getPostCategory).order_by('date_add')[:2] # [:10] if post exist
    # print(related_post)
    return render(request, 'home/post-detail.html', {
        'data': getPost,
        'post': related_post,
    })


def category_list(request):
    get_data = Category.objects.all().order_by('-date_add')
    for i in get_data:
        i.auto_not_new()
        i.auto_not_trending()
    paginator = Paginator(get_data, 30)
    pageNum = request.GET.get('page')
    data_result = paginator.get_page(pageNum)
    return render(request, 'home/category-list.html', {
        'data': data_result,
    })


def post_filter(request, id):
    try:
        getCategory = Category.objects.get(pk=id)
    except(KeyError, Category.DoesNotExist):
        redirect('home:404')
    getData = Blog.objects.filter(status=True, categorie=getCategory).order_by('date_add')
    postCount = len(getData)
    paginator = Paginator(getData, 20)
    pageNum = request.GET.get('page')
    dataresult = paginator.get_page(pageNum)
    return render(request, 'home/post-list-filter.html', {
        'category_name': getCategory,
        'data': dataresult,
        'post': postCount,
    })


def page_not_found(request):
    return render(request, 'error/404.html')