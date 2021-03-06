from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from pyforum.models import User, Forum, Thread, Post


class MyUserAdmin(UserAdmin):
    """
    """
    date_hierarchy = 'date_joined'
    search_fields = ['username']


class ForumAdmin(admin.ModelAdmin):
    """
    """
    pass


class ThreadAdmin(admin.ModelAdmin):
    """
    """
    date_hierarchy = 'time_posted'
    list_filter = ['pinned', 'highlighted', 'forum']
    search_fields = ['title']


class PostAdmin(admin.ModelAdmin):
    """
    """
    date_hierarchy = 'time_last_modified'
    list_filter = ['thread', 'user']
    search_fields = ['title']

admin.site.register(User, MyUserAdmin)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
