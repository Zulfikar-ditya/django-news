from django.urls import path

from . import views

app_name = 'reporter'

urlpatterns = [
    path('', views.reporter, name='reporter'),
]
