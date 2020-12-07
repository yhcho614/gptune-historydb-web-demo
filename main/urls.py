from django.urls import path
from django.urls import include

from . import views

from django.conf.urls import url
from django.contrib import admin

app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),
    path('acknowledgement/', views.acknowledgement, name='acknowledgement'),
    url(r'^repo/', include('repo.urls')),
    url(r'^blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    #url('^admin/', include('admin.site.urls')),
]
