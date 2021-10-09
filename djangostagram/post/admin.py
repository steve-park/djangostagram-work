from django.contrib import admin

from .models import Tag, Post

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'registered_date']


admin.site.register(Tag, TagAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'imageurl', 'registered_date']


admin.site.register(Post, PostAdmin)
