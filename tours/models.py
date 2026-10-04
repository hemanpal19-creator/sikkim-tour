from django.db import models
from destinations.models import Destination


class Tour(models.Model):
    # Basic tour information
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    # Destinations included in this tour.
    # ManyToMany is used because one tour can cover multiple destinations.
    destinations = models.ManyToManyField(
        Destination,
        related_name="tours",
        help_text="Select all destinations included in this journey.",
    )

    short_description = models.TextField()
    description = models.TextField()

    # Tour details
    duration = models.CharField(max_length=100)
    price = models.CharField(max_length=100, blank=True)

    # Optional tour image
    image = models.ImageField(
        upload_to="tours/",
        blank=True,
        null=True,
    )

    # Publishing controls
    featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name