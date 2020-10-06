from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'home/index.html')
