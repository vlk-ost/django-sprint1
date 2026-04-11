from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    # Добавьте эту строку для перевода заголовка приложения
    verbose_name = 'Блог'