from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


from home.models import Blog
from accounts.models import User
# from .form import 


def reporter(request):
    if request.user.is_authenticated and request.user.is_reporter == True:
        return render(request, 'reporter/index.html')
    else:
        return redirect('home:dont-have-access')

def my_post(request):
    if request.user.is_authenticated and request.user.is_reporter == True:
        getData = Blog.objects.filter(reporter=request.user.id)
        paginator = Paginator(getData, 20)
        pageNum = request.GET.get('page')
        data = paginator.get_page(pageNum)
        return render(request, 'reporter/mypost.html', {
            'data': data,
        })
    else:
        return redirect('home:dont-have-access')
