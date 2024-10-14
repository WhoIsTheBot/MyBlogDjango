from django.contrib import admin
from .models import Category, Article, ArticleImage

class ArticleImageInline(admin.TabularInline):  # Можна також використати StackedInline
    model = ArticleImage
    extra = 1  # Кількість пустих форм для додавання нових зображень

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    prepopulated_fields = {'slug': ('category',)}

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ArticleImageInline]  # Додаємо інлайн для зображень

admin.site.register(Article, ArticleAdmin)
