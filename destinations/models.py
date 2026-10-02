from django.db import models


class Region(models.Model):
    """
    Represents one of Sikkim's geographical regions.

    Example:
    - East Sikkim
    - West Sikkim
    - North Sikkim
    - South Sikkim

    Regions help organize destinations and create
    region-based pages later.
    """

    name = models.CharField(
        max_length=100
    )

    # Used for clean, SEO-friendly URLs.
    # Example: /destinations/east-sikkim/
    slug = models.SlugField(
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Destination(models.Model):
    """
    Represents a major tourist destination in Sikkim.

    Example:
    - Gangtok
    - Pelling
    - Lachung
    - Namchi

    A Destination belongs to one Region and can have
    multiple Attractions, Activities and Gallery Images.
    """

    name = models.CharField(
        max_length=150
    )

    # Clean URL identifier for the destination.
    # Example: /destinations/gangtok/
    slug = models.SlugField(
        unique=True
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="destinations",
    )

    # Short summary used in cards, listings and SEO-friendly previews.
    short_description = models.TextField()

    # Full destination content used on the destination detail page.
    description = models.TextField()

    best_time_to_visit = models.CharField(
        max_length=200,
        blank=True,
    )

    how_to_reach = models.TextField(
        blank=True
    )

    # Main/hero image for the destination.
    hero_image = models.ImageField(
        upload_to="destinations/",
        blank=True,
        null=True,
    )

    # Coordinates allow us to add maps/location features later.
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
    )

    # Featured destinations can be highlighted on the homepage
    # and other important landing pages.
    featured = models.BooleanField(
        default=False
    )

    # Allows us to temporarily hide a destination without deleting it.
    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Attraction(models.Model):
    """
    Represents a specific tourist attraction inside a destination.

    Example:

    Gangtok
    ├── MG Marg
    ├── Rumtek Monastery
    └── Tashi View Point

    One Destination can have many Attractions.
    """

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="attractions",
    )

    name = models.CharField(
        max_length=150
    )

    # Creates an individual SEO-friendly attraction URL later.
    # Example: /attractions/mg-marg/
    slug = models.SlugField(
        unique=True
    )

    short_description = models.TextField()

    description = models.TextField()

    image = models.ImageField(
        upload_to="destinations/attractions/",
        blank=True,
        null=True,
    )

    # Optional information that can be displayed
    # on the attraction detail page.
    best_time_to_visit = models.CharField(
        max_length=200,
        blank=True,
    )

    entry_fee = models.CharField(
        max_length=100,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Activity(models.Model):
    """
    Represents an activity or experience available at a destination.

    Example:

    Pelling
    ├── Trekking
    ├── Nature Walk
    └── Mountain Viewing

    One Destination can have many Activities.
    """

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="activities",
    )

    name = models.CharField(
        max_length=150
    )

    # Used for clean activity URLs later.
    # Example: /activities/trekking-in-pelling/
    slug = models.SlugField(
        unique=True
    )

    short_description = models.TextField()

    description = models.TextField()

    image = models.ImageField(
        upload_to="destinations/activities/",
        blank=True,
        null=True,
    )

    # Useful tourism information for activity pages.
    duration = models.CharField(
        max_length=100,
        blank=True,
    )

    best_time = models.CharField(
        max_length=150,
        blank=True,
    )

    difficulty = models.CharField(
        max_length=50,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class DestinationImage(models.Model):
    """
    Stores additional images for a destination.

    Destination.hero_image is the main hero image.
    DestinationImage provides the remaining gallery images.

    This allows every destination to have a flexible image gallery
    without storing multiple image fields directly on Destination.
    """

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="gallery_images",
    )

    image = models.ImageField(
        upload_to="destinations/gallery/"
    )

    # Optional title and alt text improve accessibility
    # and give us useful information for image SEO.
    title = models.CharField(
        max_length=150,
        blank=True,
    )

    alt_text = models.CharField(
        max_length=200,
        blank=True,
    )

    # Controls the order in which gallery images appear.
    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return f"{self.destination.name} - Image {self.id}"