from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models

from ckeditor.widgets import CKEditorWidget

from .models import Person, Role, Contact


class ContactInfoInline(admin.StackedInline):
    model = Contact
    extra = 0  # To prevent displaying extra empty forms


# Register your models here.
class PersonAdmin(UserAdmin):
    """
    user admin
    """

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "role",
    )
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "profile_image",
                    "biography",
                    "about_me",
                    "skills",
                    "slug",
                )
            },
        ),
        (("Permissions"), {"fields": ("is_active", "is_staff", "role", "groups")}),
        (("Important dates"), {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("password1", "password2"),
            },
        ),
    )

    # prepopulated_fields = {"slug": ("title",)}

    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
    }

    inlines = [ContactInfoInline]


admin.site.register(Person, PersonAdmin)
admin.site.register(Role)
