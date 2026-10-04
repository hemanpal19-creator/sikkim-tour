from django.contrib import admin
from .models import Tour


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    # Columns shown on the Tour list page.
    list_display = (
        "name",
        "duration",
        "price",
        "featured",
        "is_active",
        "created_at",
    )

    # Filters shown on the right side of the admin list.
    list_filter = (
        "featured",
        "is_active",
        "duration",
    )

    # Fields searchable from the admin search box.
    search_fields = (
        "name",
        "short_description",
        "description",
    )

    # Automatically creates the slug from the tour name.
    prepopulated_fields = {
        "slug": ("name",)
    }

    # Allows quick publishing changes from the list page.
    list_editable = (
        "featured",
        "is_active",
    )

    ordering = ("name",)

    fieldsets = (
        (
            "Tour Information",
            {
                "fields": (
                    "name",
                    "slug",
                    "destinations",
                    "short_description",
                    "description",
                )
            },
        ),
        (
            "Tour Details",
            {
                "fields": (
                    "duration",
                    "price",
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
                "classes": ("collapse",),
            },
        ),
    )

    # Timestamps are generated automatically by Django.
    readonly_fields = (
        "created_at",
        "updated_at",
    )