from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from accounts.models import User
from home.models import Category, Blog

from .forms import AddReporterForm, CategoryForm


def index(request):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True:
        return render(request, 'staff/index.html')
    else:
        return redirect('home:dont-have-access')


def list_reporter(request):
    page = 'reporter'
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True and request.user.is_active == True:
        if 'search' in request.GET:
            value = request.GET['search']
            reporter = User.objects.filter(username__contains=value, full_name__contains=value, is_reporter=True, is_staff=False, is_superuser=False)
        else:
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
    page = 'user'
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        if 'search' in request.GET:
            value = request.GET['search']
            print(value)
            user = User.objects.filter(username__contains=value, full_name__contains=value, is_reporter=False, is_staff=False, is_superuser=False)
        else:
            user = User.objects.filter(is_reporter=False, is_staff=False, is_superuser=False)
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
    if request.user.is_authenticated and request.user.is_staff == True and request.user.is_superuser == False:
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


def detail(request, username, page):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        if page == 'user':
            try:
                user = User.objects.get(username=username, is_reporter=False, is_staff=False, is_superuser=False)
            except:
                return redirect('home:404')
        elif page == 'reporter':
            try:
                user = User.objects.get(username=username, is_reporter=True, is_staff=False, is_superuser=False)
            except:
                return redirect('home:404')
        else:
            return redirect('home:404')
        return render(request, 'staff/detail.html', {
            'user': user,
            'page': page,
        })
    else:
        return redirect('home:dont-have-access')


def detail_user(request, username):
    return detail(request, username, page='user')


def detail_reporter(request, username):
    return detail(request, username, page='reporter')


def deactive_reactive(request, username, page, action):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        if page == 'user':
            try:
                user = User.objects.get(username=username, is_reporter=False, is_staff=False, is_superuser=False)
            except:
                return redirect('home:404')
        elif page == 'reporter':
            try:
                user = User.objects.get(username=username, is_reporter=True, is_staff=False, is_superuser=False)
            except:
                return redirect('home:404')
        else:
            return redirect('home:404')
        if action == 'deactive':
            user.is_active = False
            user.save()
        elif action == 'reactive':
            user.is_active = True
            user.save()
        else:
            return redirect('home:404')
        if page == 'user':
            return redirect('staff:list-user')
        else:
            return redirect('staff:list-reporter')
    else:
        return redirect('home:dont-have-access')


def deactive_confirm(request, username, page):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        if page == 'reporter' or page == 'user':
            pass
        else:
            return redirect('home:404')
        try:
            user = User.objects.get(username=username)
        except:
            return redirect('home:404')
        if user.is_active == False:
            return redirect('home:404')
        else: pass
        if page == 'reporter' and user.is_reporter == False or page == 'user' and user.is_reporter == True:
            return redirect('home:404')
        elif page == 'reporter' and user.is_reporter == True:
            pass
        return render(request, 'staff/deactive.html', {
            'user': user,
            'page': page,
            'action': 'deactive',
        })
    else:
        return redirect('home:dont-have-access')


def reactive_confirm(request, username, page):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        if page == 'reporter' or page == 'user':
            pass
        else:
            return redirect('home:404')
        try:
            user = User.objects.get(username=username)
        except:
            return redirect('home:404')
        if user.is_active == True:
            return redirect('home:404')
        else: pass
        if page == 'reporter' and user.is_reporter == False or page == 'user' and user.is_reporter == True:
            return redirect('home:404')
        elif page == 'reporter' and user.is_reporter == True:
            pass
        return render(request, 'staff/deactive.html', {
            'user': user,
            'page': page,
            'action': 'reactive',
        })
    else:
        return redirect('home:dont-have-access')


def category_list(request):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        if 'search' in request.GET:
            query = request.GET['search']
            getCate = Category.objects.filter(name__contains=query)
        else:
            getCate = Category.objects.all().order_by('-id')
        paginator = Paginator(getCate, 50)
        pageNum = request.GET.get('page')
        data = paginator.get_page(pageNum)
        return render(request, 'staff/category-list.html', {
            'data': data,
        })
    else:
        return redirect('home:dont-have-access')


def category_detail(request, id):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        try: 
            getCategory = Category.objects.get(pk=id)
        except:
            return redirect('home:404')
        return render(request, 'staff/detail-category.html', {
            'data': getCategory,
        })
    else:
        return redirect('home:dont-have-access')


'''
# if i delete a category, that make some post where have relation with category model disapear
def delete_category_confirm(request, id):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        try:
            getCategory = Category.objects.get(pk=id)
        except:
            return redirect('home:404')
        return render(request, 'staff/delete-category-confirm.html', {
            'data': getCategory,
        })
    else:
        return redirect('home:dont-have-access')


def delete_category(request, id):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        try:
            getCategory = Category.objects.get(pk=id)
        except:
            return redirect('home:404')
        getCategory.delete()
        return redirect('staff:category-list')
    else:
        return redirect('home:dont-have-access')
'''


def add_category(request):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        if request.method == 'POST':
            form = CategoryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                if 'add' in request.POST:
                    return redirect('staff:category-list')
                else:
                    return redirect('staff:add-category')
        else:
            form = CategoryForm()
        return render(request, 'staff/add-category.html', {
            'form': form,
        })
    else:
        return redirect('home:dont-have-access')


def post_by_reporter(request, username):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        try:
            user = User.objects.get(username=username)
        except:
            return redirect('home:404')
        post = Blog.objects.filter(reporter=user.id,).order_by('-id')
        paginato = Paginator(post, 50)
        pageNum = request.GET.get('page')
        data = paginato.get_page(pageNum)
        return render(request, 'staff/post-by-reporter.html', {
            'user': user,
            'data': data,
        })
    else:
        return redirect('home:dont-have-access')


def deactive_reactive_confirm_post(request, post_id, username, action):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        try:
            user = User.objects.get(username=username)
        except:
            return redirect('home:404')
        try:
            post = Blog.objects.get(pk=post_id, reporter=user.id)
        except:
            return redirect('home:404')
        if action == 'deactive' or action == 'reactive':
            pass
        else:
            return redirect('home:404')
        return render(request, 'staff/deactive-post-confirm.html', {
            'data': post,
            'user': user,
            'action': action,
        })
    else:
        return redirect('home:dont-have-access')

 
def deactive_reactive_post(request, post_id, username, action):
    if request.user.is_authenticated and request.user.is_staff == True or request.user.is_superuser == True and request.user.is_active == True:
        try:
            user = User.objects.get(username=username)
        except:
            return redirect('home:404')
        try:
            post = Blog.objects.get(pk=post_id, reporter=user.id)
        except:
            return redirect('home:404')
        else: pass
        if action == 'deactive':
            post.status = False
        elif action == 'reactive':
            post.status = True
        else:
            return redirect('home:404')
        post.save()
        return HttpResponseRedirect(f'../../../post-by-reporter/{user}/')
    else:
        return redirect('home:dont-have-access')

