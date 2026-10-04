from django.shortcuts import get_object_or_404, render

from .models import Tour


def tour_list(request):
    # Show only tours that are currently published.
    tours = Tour.objects.filter(
        is_active=True
    ).order_by("name")

    return render(
        request,
        "tours/list.html",
        {"tours": tours},
    )


def tour_detail(request, slug):
    # Find one published tour using its unique slug.
    tour = get_object_or_404(
        Tour,
        slug=slug,
        is_active=True,
    )

    return render(
        request,
        "tours/detail.html",
        {"tour": tour},
    )