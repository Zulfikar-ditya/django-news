from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User
from .forms import RegisterForm


def register(request):
    page = 'register'
    if request.user.is_authenticated:
        form = RegisterForm()
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('login'))
        else:
            form = RegisterForm()
    return render(request, 'registration/login.html', {
        'page': page,
        'form': form
    })


def my_account(request):
    if request.user.is_authenticated:
        getUser = request.user.id
        user = User.objects.get(pk=getUser)
        return render(request, 'account/index.html', {
            'user': user,
        })
    else:
        return redirect('login')


def edit_account(request):
    if request.user.is_authenticated:
        user = request.user.id
        getUser = User.objects.get(pk=user)
        if request.method == 'POST':
            try:
                getUser.avatar = request.FILES['avatar']
            except: pass
            try:
                getUser.phone = request.POST['phone']
            except: pass
            try:
                getUser.address = request.POST['address']
            except: pass
            getUser.email = request.POST['email']
            getUser.full_name = request.POST['full_name']
            getUser.gender = request.POST['gender']
            getUser.date_of_birth = request.POST['date_of_birth']
            getUser.save()
            return redirect('account:account')
        else: pass
        return render(request, 'account/edit.html', {
            'user': getUser,
        })
    else:
        return redirect('404')