from django.urls import path

from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.index, name='staff'),
    path('list-reporter/', views.list_reporter, name='list-reporter'),
    path('list-user/', views.list_user, name='list-user'),
    path("add-reporter/", views.add_reporter, name="add-reporter"),
    path('detail-user/<str:username>', views.detail_user, name='detail-user'),
    path('detail-reporter/<str:username>', views.detail_reporter, name='detail-reporter'),
    path('deactive-confirm/<str:page>/<str:username>/', views.deactive_confirm, name='delete-confirm'),
    path('deactive/<str:action>/<str:page>/<str:username>/', views.deactive_reactive, name='reactive-deactive'),
    path('reactive-confirm/<str:page>/<str:username>/', views.reactive_confirm, name='delete-confirm'),
    path('reactive/<str:action>/<str:page>/<str:username>/', views.deactive_reactive, name='reactive-deactive'),
    path('category-list/', views.category_list, name='category-list'),
    path('category-list/<int:id>/', views.category_detail, name='category-detail'),
    # path('delete-category-confirm/<int:id>/', views.delete_category_confirm, name='delete-category-confirm'),
    # path('delete-category/<int:id>/', views.delete_category, name='delete-category'),
]
