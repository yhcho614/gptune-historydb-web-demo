from django.contrib import admin

# Register your models here.
from blog.models import Post
#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'mod_date')
    list_filter = ('mod_date',)
    search_fields = ('title', 'content')
