from django.contrib import admin

from .models import Stay


@admin.register(Stay)
class StayAdmin(admin.ModelAdmin):
    # Columns shown in the stay list.
    list_display = (
        "name",
        "destination",
        "stay_type",
        "price_range",
        "featured",
        "is_active",
        "created_at",
    )

    # Quick filtering from the sidebar.
    list_filter = (
        "destination",
        "stay_type",
        "featured",
        "is_active",
    )

    # Search across useful stay information.
    search_fields = (
        "name",
        "short_description",
        "description",
        "destination__name",
    )

    # Generate the URL slug from the stay name.
    prepopulated_fields = {
        "slug": ("name",),
    }

    # Quickly publish/unpublish or feature a stay.
    list_editable = (
        "featured",
        "is_active",
    )

    ordering = (
        "destination",
        "name",
    )

    fieldsets = (
        (
            "Stay Information",
            {
                "fields": (
                    "destination",
                    "name",
                    "slug",
                    "short_description",
                    "description",
                )
            },
        ),
        (
            "Accommodation Details",
            {
                "fields": (
                    "stay_type",
                    "price_range",
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

    # These values are generated automatically by Django.
    readonly_fields = (
        "created_at",
        "updated_at",
    )