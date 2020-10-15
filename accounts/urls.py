from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.my_account, name='account'),
    path('edit/', views.edit_account, name='edit'),
    path('register/', views.register, name='register'),
]
