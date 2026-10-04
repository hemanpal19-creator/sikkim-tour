from django.db import models

from destinations.models import Destination


class Stay(models.Model):
    # Name displayed on stay cards and detail pages.
    name = models.CharField(max_length=200)

    # SEO-friendly URL identifier.
    slug = models.SlugField(unique=True)

    # Destination where this stay is located.
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="stays",
    )

    # Short introduction for listing cards.
    short_description = models.TextField()

    # Full description for the stay detail page.
    description = models.TextField()

    # Type of accommodation.
    stay_type = models.CharField(max_length=100)

    # Approximate pricing shown to visitors.
    price_range = models.CharField(max_length=100, blank=True)

    # Main stay image.
    image = models.ImageField(
        upload_to="stays/",
        blank=True,
        null=True,
    )

    # Publishing controls.
    featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Automatically maintained timestamps.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name