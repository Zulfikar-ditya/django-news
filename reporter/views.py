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
