from django.contrib import admin
from .models import Blog, Category, Keyword


class KeywordsInline(admin.TabularInline):
    model = Keyword


class BlogAdmin(admin.ModelAdmin):
    inlines = (KeywordsInline,)


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
