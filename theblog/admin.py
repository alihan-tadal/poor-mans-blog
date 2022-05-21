from django.contrib import admin
from theblog.models import Category, Post


# Register your models here.
admin.site.register(Post)
admin.site.register(Category)