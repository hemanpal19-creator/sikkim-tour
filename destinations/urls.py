from django.urls import path

from . import views


urlpatterns = [
    # Attraction listing page.
    # Example: /destinations/attractions/
    path(
        "attractions/",
        views.attraction_list,
        name="attraction_list",
    ),

    # Attraction detail page.
    # Example: /destinations/attractions/mg-marg/
    path(
        "attractions/<slug:slug>/",
        views.attraction_detail,
        name="attraction_detail",
    ),

    # Destination detail page.
    # Example: /destinations/gangtok/
    path(
        "<slug:slug>/",
        views.destination_detail,
        name="destination_detail",
    ),
]