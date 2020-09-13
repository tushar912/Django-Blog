from django.urls import path
from django.conf.urls import url
from . import views

<<<<<<< HEAD
app_name = 'articles'
urlpatterns = [
   
    url(r'^$', views.article_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail,name='detail'),
=======
app_name = 'article'

urlpatterns = [
    path('', views.article_list,name='list'),
    path('<slug:slug>/', views.article_detail,name='detail'),
>>>>>>> new
]