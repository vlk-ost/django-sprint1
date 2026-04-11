from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category

def get_base_post_queryset():
    """Функция для получения базового запроса с фильтрацией."""
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )

def index(request):
    template = 'blog/index.html'
    # Вызываем функцию, чтобы получить актуальное время на момент запроса
    post_list = get_base_post_queryset().order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)

def post_detail(request, id):
    template = 'blog/detail.html'
    # Используем актуальный QuerySet для поиска конкретного поста
    post = get_object_or_404(get_base_post_queryset(), pk=id)
    context = {'post': post}
    return render(request, template, context)

def category_posts(request, category_slug):
    template = 'blog/category.html'
    # Находим опубликованную категорию
    category = get_object_or_404(
        Category, 
        slug=category_slug, 
        is_published=True
    )
    # Фильтруем посты этой категории через наш базовый запрос
    post_list = get_base_post_queryset().filter(category=category).order_by('-pub_date')
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)