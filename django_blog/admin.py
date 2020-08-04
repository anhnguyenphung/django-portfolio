from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django_blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)