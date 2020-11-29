from django.urls import path

from . import views

app_name = "repo"
urlpatterns = [
    path('', views.index, name='index'),
    path('upload_cli/', views.UploadView.as_view(), name='upload'),
    path('upload/', views.upload, name='upload'),
    path('perf_upload/', views.perf_upload, name='perf_upload'),
    path('<int:perf_file_id>/', views.query, name='query'),
]
