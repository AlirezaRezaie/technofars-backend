from django.contrib import admin
from .models import Blog, Category, Keyword


class KeywordsInline(admin.TabularInline):
    model = Keyword


class BlogAdmin(admin.ModelAdmin):
    inlines = (KeywordsInline,)
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
