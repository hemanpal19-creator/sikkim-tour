from django.contrib import admin

from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    """
    Admin interface for managing visitor journey enquiries.
    """

    list_display = (
        "name",
        "email",
        "phone",
        "travel_date",
        "travelers",
        "created_at",
    )

    list_filter = (
        "travel_date",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "message",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )