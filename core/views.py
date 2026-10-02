from django.shortcuts import render

from destinations.models import Destination


def home(request):
    # Homepage destinations come from the database so the content
    # can be managed through Django Admin instead of editing HTML.
    destinations = (
        Destination.objects
        .filter(is_active=True)
        .order_by("-featured", "name")[:6]
    )

    return render(
        request,
        "core/home.html",
        {
            "destinations": destinations,
        },
    )