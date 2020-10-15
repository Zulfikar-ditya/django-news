from django.shortcuts import render, redirect
from django.core import paginator
from django.http import HttpResponseRedirect


def index(request):
    if request.user.is_authenticated && request.user.is_staff == True && request.user.is_superuser = True:
        return render(request, 'staff/index.html')
    else:
        return redirect('home:404')
