from django.urls import path

from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.index, name='staff'),
    path('list-reporter/', views.list_reporter, name='list-reporter'),
    path('list-user/', views.list_user, name='list-user'),
    path("add-reporter/", views.add_reporter, name="add-reporter"),
]
