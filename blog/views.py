from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, TodayArchiveView, YearArchiveView, MonthArchiveView, DayArchiveView

from blog.models import Post

# Create your views here.

class PostLV(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 2

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'mod_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'mod_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'mod_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'mod_date'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'mod_date'

def create(request):
    return render(request, 'blog/post_create.html')

from django.shortcuts import redirect
from datetime import datetime
from django.urls import reverse_lazy

def postcreate(request):
    post = Post()

    post.title = request.GET['title']
    post.content = request.GET['body']
    post.pub_date = datetime.now()
    post.mod_date = datetime.now()
    post.save()

    return redirect(reverse_lazy('blog:post_archive'))
