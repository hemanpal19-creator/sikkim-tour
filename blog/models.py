from django.db import models


class Post(models.Model):
    # Main title shown on the journal page.
    title = models.CharField(max_length=200)

    # Unique URL for each journal article.
    slug = models.SlugField(unique=True)

    # Short introduction used on listing pages.
    short_description = models.TextField()

    # Full article content.
    content = models.TextField()

    # Optional article image.
    image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True,
    )

    # Featured articles can be highlighted on the website.
    featured = models.BooleanField(default=False)

    # Allows unpublished articles to stay hidden from visitors.
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title