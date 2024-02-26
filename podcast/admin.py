from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Podcast


class PodcastAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
    }


admin.site.register(Podcast, PodcastAdmin)
