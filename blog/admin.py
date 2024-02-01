from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Blog, Category, Keyword


class KeywordsInline(admin.TabularInline):
    model = Keyword


class BlogAdmin(admin.ModelAdmin):
    inlines = (KeywordsInline,)
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
    }


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
