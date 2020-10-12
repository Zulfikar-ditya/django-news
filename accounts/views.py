from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

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

