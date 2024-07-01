from django.contrib import admin
from .models import Post, Category

admin.site.site_header = "Grumpy Blog Admin"

admin.site.register(Post)
admin.site.register(Category)