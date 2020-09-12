
from django.contrib import admin
from django.urls import path

urlpatterns = [
     url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),
]
