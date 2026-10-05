from django.shortcuts import render

from destinations.models import Destination, Activity
from tours.models import Tour
from blog.models import Post
from stays.models import Stay
from enquiries.forms import EnquiryForm

def home(request):
    """
    Loads the featured content needed for the homepage.

    Only a small selection is displayed here so the homepage stays
    visually focused while the full content remains available through
    the dedicated listing pages.
    """

    destinations = (
        Destination.objects
        .filter(is_active=True)
        .order_by("-featured", "name")[:6]
    )

    journeys = (
        Tour.objects
        .filter(is_active=True)
        .order_by("-featured", "name")[:3]
    )

    experiences = (
        Activity.objects
        .filter(is_active=True)
        .order_by("name")[:4]
    )
    
    journal_posts = (
        Post.objects
        .filter(is_active=True)
        .order_by("-created_at")[:3]
    )
    
    stays = (
        Stay.objects
        .filter(is_active=True)
        .order_by("-featured", "name")[:3]
    )

    form = EnquiryForm()
    
    return render(
        request,
        "core/home.html",
        {
            "destinations": destinations,
            "journeys": journeys,
            "experiences": experiences,
            "journal_posts": journal_posts,
            "stays": stays,
            "form": form,
        },
    )