from django.contrib import admin
from .models import Post, Category, Location

# Регистрация моделей, чтобы они появились в панели управления
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Location)