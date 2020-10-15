from django.urls import path

from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.index, name='staff'),
    path('list-reporter/', views.list_reporter, name='list-reporter')
]
