from django.shortcuts import get_object_or_404, render

from .models import Destination, Attraction


def destination_detail(request, slug):
    """
    Displays one destination using its unique slug.

    Example:
    /destinations/gangtok/
    """

    # Find the requested destination.
    # If it doesn't exist or is inactive, Django returns a 404 page.
    destination = get_object_or_404(
        Destination,
        slug=slug,
        is_active=True,
    )

    # Send the destination object to the reusable detail template.
    return render(
        request,
        "destinations/detail.html",
        {
            "destination": destination,
        },
    )


def attraction_detail(request, slug):
    """
    Displays one attraction using its unique slug.

    Example:
    /attractions/mg-marg/
    """

    # Find the attraction using its unique slug.
    # Only active attractions are publicly accessible.
    attraction = get_object_or_404(
        Attraction,
        slug=slug,
        is_active=True,
    )

    # Send the attraction object to its reusable detail template.
    return render(
        request,
        "destinations/attraction_detail.html",
        {
            "attraction": attraction,
        },
    )
    
    
# Why?

# We don't want six separate views such as:

# gangtok()
# pelling()
# lachung()
# ...

# One view handles every destination.