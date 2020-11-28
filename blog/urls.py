from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    path('post/create', views.create, name='create'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('post/', views.PostLV.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDV.as_view(), name='post_detail'),
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    path('archive/<int:year>', views.PostYAV.as_view(), name='post_year_archive'),
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),
    path('archive/today/', views.PostTAV.as_view(), name='post_today'),
]
