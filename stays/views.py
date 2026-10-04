from django.shortcuts import get_object_or_404, render

from .models import Stay


def stay_list(request):
    # Show only published stays.
    stays = Stay.objects.filter(
        is_active=True
    ).select_related(
        "destination"
    ).order_by("name")

    return render(
        request,
        "stays/list.html",
        {"stays": stays},
    )


def stay_detail(request, slug):
    # Find one published stay using its unique slug.
    stay = get_object_or_404(
        Stay.objects.select_related("destination"),
        slug=slug,
        is_active=True,
    )

    return render(
        request,
        "stays/detail.html",
        {"stay": stay},
    )