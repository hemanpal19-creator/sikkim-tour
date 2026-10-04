from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "featured",
        "is_active",
        "created_at",
    )

    list_filter = (
        "featured",
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "short_description",
        "content",
    )

    # Automatically creates the URL slug from the title.
    prepopulated_fields = {
        "slug": ("title",),
    }

    # Allows quick publishing/feature changes from the list.
    list_editable = (
        "featured",
        "is_active",
    )

    ordering = (
        "-created_at",
    )

    fieldsets = (
        (
            "Article Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "short_description",
                    "content",
                )
            },
        ),
        (
            "Image",
            {
                "fields": (
                    "image",
                )
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "featured",
                    "is_active",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )