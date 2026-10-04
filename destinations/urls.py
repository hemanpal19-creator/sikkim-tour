from django.urls import path

from . import views


urlpatterns = [
    # Attraction listing page.
    path(
        "attractions/",
        views.attraction_list,
        name="attraction_list",
    ),

    # Attraction detail page.
    path(
        "attractions/<slug:slug>/",
        views.attraction_detail,
        name="attraction_detail",
    ),

    # Activity listing page.
    # Example: /destinations/activities/
    path(
        "activities/",
        views.activity_list,
        name="activity_list",
    ),

    # Activity detail page.
    # Example: /destinations/activities/trekking/
    path(
        "activities/<slug:slug>/",
        views.activity_detail,
        name="activity_detail",
    ),

    # Destination listing page.
    # Example: /destinations/
    path(
        "",
        views.destination_list,
        name="destination_list",
    ),
    
    # Destination detail page.
    # Example: /destinations/gangtok/
    path(
        "<slug:slug>/",
        views.destination_detail,
        name="destination_detail",
    ),
]