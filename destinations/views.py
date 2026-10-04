from django.shortcuts import get_object_or_404, render

from .models import Destination, Attraction, Activity
from tours.models import Tour
from stays.models import Stay


def destination_list(request):
    """
    Displays all active destinations.

    Destinations are loaded from the database so the page
    automatically updates when content is managed through Django Admin.
    """

    destinations = (
        Destination.objects
        .filter(is_active=True)
        .order_by("-featured", "name")
    )

    return render(
        request,
        "destinations/list.html",
        {
            "destinations": destinations,
        },
    )

def destination_detail(request, slug):
    # Find the requested active destination.
    destination = get_object_or_404(
        Destination,
        slug=slug,
        is_active=True,
    )

    # Load journeys connected to this destination.
    journeys = (
        Tour.objects
        .filter(
            destinations=destination,
            is_active=True,
        )
        .order_by("-featured", "name")[:4]
    )

    # Load stays located in this destination.
    stays = (
        Stay.objects
        .filter(
            destination=destination,
            is_active=True,
        )
        .order_by("-featured", "name")[:4]
    )

    return render(
        request,
        "destinations/detail.html",
        {
            "destination": destination,
            "journeys": journeys,
            "stays": stays,
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
    
def attraction_list(request):
    """
    Displays all active attractions.

    The attractions are taken directly from the database,
    so whenever we add a new attraction through Django Admin,
    it can automatically appear on this page.
    """

    # Get only attractions that are currently active.
    # Ordering by name keeps the listing organized.
    attractions = Attraction.objects.filter(
        is_active=True
    ).order_by("name")

    # Send the attractions to the listing template.
    return render(
        request,
        "destinations/attraction_list.html",
        {
            "attractions": attractions,
        },
    )
    
def activity_detail(request, slug):
    """
    Displays one activity using its unique slug.

    Example:
    /destinations/activities/trekking/
    """

    # Find the requested active activity by its unique slug.
    activity = get_object_or_404(
        Activity,
        slug=slug,
        is_active=True,
    )

    # Send the activity to the reusable detail template.
    return render(
        request,
        "destinations/activity_detail.html",
        {
            "activity": activity,
        },
    )


def activity_list(request):
    """
    Displays all active activities.

    Activities are loaded from the database, so new activities
    added through Django Admin automatically appear here.
    """

    # Get all active activities and keep them alphabetically ordered.
    activities = Activity.objects.filter(
        is_active=True
    ).order_by("name")

    return render(
        request,
        "destinations/activity_list.html",
        {
            "activities": activities,
        },
    )
    
# Why?

# We don't want six separate views such as:

# gangtok()
# pelling()
# lachung()
# ...

# One view handles every destination.