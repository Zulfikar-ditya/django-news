from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from accounts.models import User

from .forms import AddReporterForm


def index(request):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True:
        return render(request, 'staff/index.html')
    else:
        return redirect('home:dont-have-access')


def list_reporter(request):
    page = 'reporter'
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True:
        reporter = User.objects.filter(is_reporter=True, is_staff=False, is_superuser=False).order_by('id')
        paginator = Paginator(reporter, 100)
        pageNum = request.GET.get('page')
        data = paginator.get_page(pageNum)
        return render(request, 'staff/list-user.html', {
            'data': data,
            'page': page,
        })
    else:
        return redirect('home:dont-have-access')


def list_user(request):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True:
        user = User.objects.filter(is_reporter=False, is_staff=False, is_superuser=False)
        page = 'user'
        paginator = Paginator(user, 100)
        pageNum = request.GET.get('page')
        data = paginator.get_page(pageNum)
        return render(request, 'staff/list-user.html', {
            'data': data,
            'page': page
        })
    else:
        return redirect('home:dont-have-access')


def add_reporter(request):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True:
        if request.method == 'POST':
            form = AddReporterForm(request.POST, request.FILES)
            if form.is_valid():
                instace = form.save(commit=False)
                instace.is_reporter = True
                instace.save()
                if 'add' in request.POST:
                    return redirect('staff:list-reporter')
                else:
                    return redirect('staff:add-reporter')
        else:
            form = AddReporterForm()
        return render(request, 'staff/add-reporter.html', {
            'form': form,
        })
    else:
        return redirect('home:dont-have-access')
