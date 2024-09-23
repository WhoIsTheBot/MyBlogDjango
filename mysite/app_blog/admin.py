from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    prepopulated_fields = {'slug': ('category',)}  # Додаємо автозаповнення

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
