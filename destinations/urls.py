from django.urls import path

from . import views


urlpatterns = [
    # One URL pattern handles every destination using its slug.
    # Example: /destinations/gangtok/
    path(
        "<slug:slug>/",
        views.destination_detail,
        name="destination_detail",
    ),

    # One URL pattern handles every attraction using its slug.
    # Example: /destinations/attractions/mg-marg/
    path(
        "attractions/<slug:slug>/",
        views.attraction_detail,
        name="attraction_detail",
    ),
]