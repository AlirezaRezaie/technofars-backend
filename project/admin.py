from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = (ProjectImageInline,)
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
    }


admin.site.register(Project, ProjectAdmin)
