from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from accounts.models import User


def index(request):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True:
        return render(request, 'staff/index.html')
    else:
        return redirect('home:dont-have-access')


def list_reporter(request):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True:
        reporter = User.objects.filter(is_reporter=True, is_staff=False, is_superuser=False).order_by('id')
        paginator = Paginator(reporter, 100)
        pageNum = request.GET.get('page')
        data = paginator.get_page(pageNum)
        return render(request, 'staff/list-user.html', {
            'data': data,
        })
    else:
        return redirect('home:dont-have-access')