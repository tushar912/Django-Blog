from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'articl'

urlpatterns = [
    path('', views.article_list,name='list'),
    path('create/',views.article_create,name='create'),
    path('<slug:slug>/', views.article_detail,name='detail'),
]