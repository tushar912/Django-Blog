from django.conf.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
]