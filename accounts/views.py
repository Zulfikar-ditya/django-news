from django.shortcuts import render, redirect

from .forms import RegisterForm

def register(request):
    page = 'register'
    if request.user.is_authenticated:
        form = RegisterForm()
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid:
                form.save()
                redirect('login')
        else:
            form = RegisterForm()
    return render(request, 'registration/login.html', {
        'page': page,
        'form': form
    })

