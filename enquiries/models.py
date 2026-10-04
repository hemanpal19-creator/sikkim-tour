from django.db import models


class Enquiry(models.Model):
    """
    Stores journey planning enquiries submitted by website visitors.
    """

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20, blank=True)

    travel_date = models.DateField(
        null=True,
        blank=True,
    )

    travelers = models.PositiveIntegerField(
        default=1,
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.email}"