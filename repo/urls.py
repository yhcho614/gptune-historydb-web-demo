from django.urls import path

from . import views

app_name = "repo"
urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.UpdateView.as_view(), name='update'),
    path('<int:perf_file_id>/', views.query, name='query'),
]
