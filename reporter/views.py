from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


from home.models import Blog, Category
from accounts.models import User
from .forms import BlogForm


def reporter(request):
    if request.user.is_authenticated and request.user.is_reporter == True:
        return render(request, 'reporter/index.html')
    else:
        return redirect('home:dont-have-access')


def my_post(request):
    if request.user.is_authenticated and request.user.is_reporter == True:
        getData = Blog.objects.filter(reporter=request.user.id, status=True)
        paginator = Paginator(getData, 20)
        pageNum = request.GET.get('page')
        data = paginator.get_page(pageNum)
        return render(request, 'reporter/mypost.html', {
            'data': data,
        })
    else:
        return redirect('home:dont-have-access')


def choose_category(request):
    if request.user.is_authenticated and request.user.is_reporter == True and request.user.is_active == True and request.user.is_staff == False:
        getCategori = Category.objects.all().order_by('-date_add')
        paginator = Paginator(getCategori, 50)
        pageNum = request.GET.get('page')
        data = paginator.get_page(pageNum)
        return render(request, 'reporter/choose-category.html', {
            'data': data,
        })
    else:
        return redirect('home:dont-have-access')    


def add_post(request, id):
    if request.user.is_authenticated and request.user.is_reporter == True and request.user.is_active == True and request.user.is_staff == False:
        try: 
            getCategory = Category.objects.get(pk=id)
        except (KeyError, Category.DoesNotExist):
            return redirect('home:404')
        form = BlogForm()
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.reporter = request.user
                instance.categorie = getCategory
                form.save()
                if 'add' in request.POST:
                    return redirect('reporter:my-post')
                else:
                    return HttpResponseRedirect(f'../{getCategory.id}/')
        else:
            form = BlogForm()
        return render(request, 'reporter/add.html', {
            'form': form,
            'data': getCategory,
        })
    else:
        return redirect('home:dont-have-access')


def edit_post(request, id):
    if request.user.is_authenticated and request.user.is_reporter == True and request.user.is_active == True and request.user.is_staff == False:
        getCategory = Category.objects.all()
        try:
            getPost = Blog.objects.get(pk=id, reporter=request.user, status=True)
        except:
            return redirect('home:404')
        if request.method == "POST":
            get_title = request.POST['title']
            get_category = request.POST['category']
            get_Content = request.POST['content']
            try:
                getImage = request.FILES['image']
                getPost.image = getImage
            except: pass
            getPost.title = get_title
            getPost.categorie = Category.objects.get(name=get_category)
            getPost.content = get_Content
            getPost.save()
            return redirect('reporter:my-post')
        return render(request, 'reporter/edit.html', {
            'data': getPost,
            'category': getCategory,
        })
    else:
        return redirect('home:dont-have-access')

    
def delete_post_confirm(request, id):
    if request.user.is_authenticated and request.user.is_reporter == True and request.user.is_active == True and request.user.is_staff == False:
        try:
            getPost = Blog.objects.get(pk=id, reporter=request.user, status=True)
        except:
            return redirect('home:404')
        return render(request, 'reporter/delete-confirm.html', {
            'data': getPost,
        })
    else:
        return redirect('home:dont-have-access')



def delete_post(request, id):
    if request.user.is_authenticated and request.user.is_reporter == True and request.user.is_active == True and request.user.is_staff == False:
        try:
            getPost = Blog.objects.get(pk=id, reporter=request.user, status=True)
        except:
            return redirect('home:404')
        getPost.status = False
        getPost.save()
        return redirect('reporter:my-post')
    else:
        return redirect('home:dont-have-access')