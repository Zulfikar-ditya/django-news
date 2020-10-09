from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.post_detail, name='post-detail'),
    path('category-list/', views.category_list, name='category-list'),
    path('post-by-category/<int:id>/', views.post_filter, name='post-filter'),

    path('404/', views.page_not_found, name='404'),
]
