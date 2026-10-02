from django.shortcuts import get_object_or_404, render
from .models import Destination

# Create your views here.

def destination_detail(request, slug):
    # Find the destination using its unique slug.
    # If the slug does not exist, Django automatically shows a 404 page.
    destination = get_object_or_404(
        Destination,
        slug=slug,
        is_active=True,
    )

    # Send the selected destination to one reusable template.
    return render(
        request,
        "destinations/detail.html",
        {
            "destination": destination,
        },
    )
    
    
    
# Why?

# We don't want six separate views such as:

# gangtok()
# pelling()
# lachung()
# ...

# One view handles every destination.