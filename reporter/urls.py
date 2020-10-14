from django.urls import path

from . import views

app_name = 'reporter'

urlpatterns = [
    path('', views.reporter, name='reporter'),
    path('my-post/', views.my_post, name='my-post'),
    path('add-post/', views.choose_category, name='choose-category'),
    path('add-post/<int:id>/', views.add_post, name='add-post'),
    path('edit-post/<int:id>/', views.edit_post, name='edit-post'),
]
